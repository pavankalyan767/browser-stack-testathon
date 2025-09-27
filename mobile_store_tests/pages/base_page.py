# Contains reusable methods for all pages
class BasePage:
    def click(self, locator): pass           # Click any element
    def enter_text(self, locator, text): pass # Type into fields
    def get_text(self, locator): pass        # Get text from elements
    # These methods handle waiting and error handling for you