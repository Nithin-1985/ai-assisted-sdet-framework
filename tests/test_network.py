from playwright.sync_api import expect


def test_observe_network(page):
    page.on(
        "response",
        lambda response: print(
            response.status,
            response.url
        )
    )

    page.goto("https://www.saucedemo.com/")


def test_wait_for_specific_response(page):
    page.goto("https://www.saucedemo.com/")

    with page.expect_response(
        lambda response: "/users/1" in response.url
    ) as response_info:

        page.evaluate("""
            fetch("https://jsonplaceholder.typicode.com/users/1")
        """)

    response = response_info.value

    print("Status:", response.status)
    print("URL:", response.url)
    body = response.json()
    assert response.status == 200
    assert body["id"] == 1
    assert body["name"] == "Leanne Graham"

def test_inspect_post_request(page):
    page.goto("https://www.saucedemo.com/")

    with page.expect_request(
        lambda request: (
            "/posts" in request.url
            and request.method == "POST"
        )
    ) as request_info:

        page.evaluate("""
            fetch("https://jsonplaceholder.typicode.com/posts", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    title: "Playwright Network Test",
                    body: "Learning request inspection",
                    userId: 1
                })
            })
        """)

    request = request_info.value
    payload = request.post_data_json

    assert request.method == "POST"
    assert payload["title"] == "Playwright Network Test"
    assert payload["userId"] == 1

def test_post_request_and_response(page):
    page.goto("https://www.saucedemo.com/")

    with page.expect_request(
        lambda request: (
            "/posts" in request.url
            and request.method == "POST"
        )
    ) as request_info:

        with page.expect_response(
            lambda response: (
                "/posts" in response.url
                and response.request.method == "POST"
            )
        ) as response_info:

            page.evaluate("""
                fetch("https://jsonplaceholder.typicode.com/posts", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        title: "Network Test",
                        body: "Request and response",
                        userId: 1
                    })
                })
            """)

    request = request_info.value
    response = response_info.value

    request_payload = request.post_data_json
    response_body = response.json()

    assert request.method == "POST"
    assert request_payload["title"] == "Network Test"

    assert response.status == 201
    assert response_body["title"] == "Network Test"


def test_intercept_and_abort(page):

    def handle_route(route):
        print("Blocking:", route.request.url)
        route.abort()

    page.route("**/posts", handle_route)

    page.goto("https://www.saucedemo.com/")

    page.evaluate("""
        fetch("https://jsonplaceholder.typicode.com/posts")
    """)

def test_mock_response(page):

    def handle_route(route):
        route.fulfill(
            status=200,
            content_type="application/json",
            body='{"name": "Nithin", "role": "admin"}'
        )

    page.route("**/users/1", handle_route)

    page.goto("https://www.saucedemo.com/")

    result = page.evaluate("""
        fetch("https://jsonplaceholder.typicode.com/users/1")
            .then(response => response.json())
    """)

    print(result)

def test_mock_api_for_ui(page):

    def handle_route(route):
        response = route.fetch()
        body = response.json()
        print("Real name:", body["name"])

        body["name"] = "Nithin"

        route.fulfill(
            response=response,
            json=body
        )

    page.route("**/users/1", handle_route)

    page.set_content("""
    <button onclick="loadUser()">Load User</button>
    <div id="result"></div>

    <script>
        async function loadUser() {
            const response = await fetch(
                "https://jsonplaceholder.typicode.com/users/1"
            );

            const data = await response.json();

            document.getElementById("result").innerText = data.name;
        }
    </script>
    """)
    page.get_by_role("button", name="Load User").click()
    expect(page.get_by_text("Nithin")).to_be_visible()
