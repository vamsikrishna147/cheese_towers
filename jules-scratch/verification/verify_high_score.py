
from playwright.sync_api import sync_playwright
import os

def run_verification():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Construct the file path to index.html
        file_path = "file://" + os.path.abspath("index.html")
        page.goto(file_path)

        # Click the play button
        page.click("#play-button")

        # Wait for the in-game UI to be visible
        page.wait_for_selector("#in-game-ui", state="visible")

        # Play the game for a bit
        for _ in range(5):
            page.wait_for_timeout(200)
            page.click("#in-game-ui")

        # Intentionally lose the game
        # Click far to the side to miss the stack
        page.mouse.click(10, 10)

        # Wait for the game over screen
        page.wait_for_selector("#game-over-screen", state="visible")

        # Take a screenshot
        page.screenshot(path="jules-scratch/verification/verification.png")

        browser.close()

if __name__ == "__main__":
    run_verification()
