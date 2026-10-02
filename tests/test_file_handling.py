from playwright.sync_api import Page, expect



def test_file_upload(page: Page):

    page.set_content("""
        <h1>File Upload</h1>
        <input type="file">
        <button>Upload</button>
    """)

    file_input = page.locator('input[type="file"]')

    file_input.set_input_files(
        "test_data/sample_upload.txt"
    )

    selected_file = file_input.evaluate(
    "input => input.files[0].name"
    )

    assert selected_file == "sample_upload.txt"

def test_file_download(page: Page, tmp_path):
    page.goto(
        "https://app.thetestingacademy.com/playwright/widgets/upload-download"
    )
   

    with page.expect_download() as download_info:
        page.get_by_role("button",name="Download text file").click()

    download = download_info.value

    download_path = tmp_path / download.suggested_filename

    download.save_as(download_path)

    assert download_path.exists()
    assert download_path.stat().st_size > 0
    file_content = download_path.read_text()
    assert "The Testing Academy — sample download." in file_content

# Kept commented because the-internet.herokuapp.com can be unreliable.

# def test_file_upload_real_website(page: Page):
#     page.goto(
#         "https://the-internet.herokuapp.com/upload",
#         wait_until="domcontentloaded"
#     )
#
#     file_input = page.locator("#file-upload")
#
#     file_input.set_input_files(
#         "test_data/sample_upload.txt"
#     )
#
#     page.locator("#file-submit").click()
#
#     expect(page.get_by_text("File Uploaded!")).to_be_visible()
#
#     expect(
#         page.locator("#uploaded-files")
#     ).to_have_text("sample_upload.txt")
