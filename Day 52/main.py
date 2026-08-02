  def find_followers(self):
        self.driver.get(f"{BASE_URL}/u/{SIMILAR_ACCOUNT}/followers")
        time.sleep(2)

        # The scrollable element inside the followers dialog. Inspect to confirm the class.
        modal = self.driver.find_element(By.CSS_SELECTOR, ".followers-scroll")
        for _ in range(10):
            # "scroll this element to the bottom" → loads the next batch of followers
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(1)