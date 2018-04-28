from time import sleep, mktime
from datetime import datetime
from Armis import SLEEP


class Playlists:
    def __init__(self, test):
        self.browser = test.browser
        # Unique, based on UNIX timestamp
        self.id = str(int(mktime(datetime.utcnow().timetuple())))[3:]
        self.navigate()
        self.playlists = []
        self.playlists_scrape()

    def playlists_scrape(self):
        """
        Updates the list of available playlists
        """
        self.browser.refresh()
        sleep(SLEEP)
        playlists = [pl.get_attribute('textContent') for pl in self.browser.find_elements_by_class_name('tile_title')]
        self.playlists = [p.split('\n')[1].replace(' ', '') for p in playlists]
        sleep(SLEEP)

    def navigate(self):
        """
        Goes to Playlists tab
        """
        sleep(SLEEP)
        self.browser.find_element_by_class_name("playlist-btn-container").click()
        self.browser.find_element_by_link_text("View track's page").click()
        sleep(SLEEP+2)
        self.browser.find_element_by_link_text("Playlists").click()

    def add_playlist(self):
        """
        Creating a new playlist with self.id as title
        """
        self.browser.find_element_by_class_name('orfium-playlist-add').click()
        sleep(SLEEP)
        self.browser.find_element_by_class_name('playlist-create').click()
        self.browser.find_element_by_class_name('playlist-title').send_keys(self.id)
        self.browser.find_element_by_class_name('playlist-create-button').click()
        print (self.id + ' Was added as a new Playlist')

    def test_add_pl(self):
        """
        Asserting a new playlist was added
        """
        side_bar_count = int(self.count_playlists())
        self.add_playlist()
        sleep(SLEEP)
        self.browser.find_element_by_link_text("Playlists").click()
        self.playlists_scrape()
        # In record's list of playlists
        try:
            assert (self.id == self.playlists[-1])
        except AssertionError:
            raise AssertionError(self.id + ' Is not the newest playlist')
        # In side bar's list of playlists
        try:
            assert (side_bar_count == int(self.count_playlists()) - 1)
        except AssertionError:
            raise AssertionError(self.id + ' Is not found in the side bar')

    def count_playlists(self):
        self.browser.maximize_window()
        sleep(2)
        pl_sidebar_xpath = '/html/body/div[2]/div[1]/div/aside[2]/div/div[1]/div[2]/div[2]'
        return self.browser.find_element_by_xpath(pl_sidebar_xpath).get_attribute('childElementCount')
