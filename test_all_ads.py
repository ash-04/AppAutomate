import logging
import pytest
from Page_Objects.Ads.page_ads import PageAds
from Launcher.berlin_launcher import BerlinLauncher
from Utilities.general_utils import custom_logger


@pytest.mark.usefixtures('page_objects')
class TestAllAds:
    @pytest.fixture(scope='class')
    def page_objects(self,  request, pytestconfig, browser, region, os, platform, env, url, test_run_id):
        print('env:', env)
        print("region", region)

        be_obj = BerlinLauncher()
        request.cls.be_obj = be_obj
        request.cls.obj = be_obj.launch_berlin_game(browser, os, platform, env, url)
        request.cls.page_ads_obj = PageAds()
        request.cls.log = custom_logger(logging.INFO)
        test_run_id = None if test_run_id == 'None' else test_run_id
        if test_run_id:
            request.cls.test_run_id = test_run_id
        else:
            request.cls.test_run_id = None
        yield
        del request.cls.be_obj

    # Test case starts from here


    @pytest.mark.edge_windows_desktop
    @pytest.mark.chrome_windows_desktop
    @pytest.mark.safari_macOS_desktop
    @pytest.mark.chrome_macOS_desktop
    @pytest.mark.prod
    @pytest.mark.staging
    @pytest.mark.qa
    @pytest.mark.run(order=2500)
    def test_preroll_ad_visible(self, case_id=8843489):
        """BERLIN::Ads --->C8843489: Verify pre-roll ads for android games"""
        assert self.page_ads_obj.verify_pre_roll_ads(self.obj, self.test_run_id, case_id) is True

    @pytest.mark.edge_windows_desktop
    @pytest.mark.chrome_windows_desktop
    @pytest.mark.safari_macOS_desktop
    @pytest.mark.chrome_macOS_desktop
    @pytest.mark.prod
    @pytest.mark.staging
    @pytest.mark.qa
    @pytest.mark.run(order=2501)
    def test_midroll_display_ad_visible(self, case_id=8968250):
        """BERLIN::Ads --->C8968250: Verify midroll display ads for android games """
        assert self.page_ads_obj.verify_midroll_display_ads(self.obj, self.test_run_id, case_id) is True

    @pytest.mark.edge_windows_desktop
    @pytest.mark.chrome_windows_desktop
    @pytest.mark.safari_macOS_desktop
    @pytest.mark.chrome_macOS_desktop
    @pytest.mark.prod
    @pytest.mark.staging
    @pytest.mark.qa
    @pytest.mark.run(order=2502)
    def test_midroll_video_ad_visible(self, case_id=8968251):
        """BERLIN::Ads --->C8968251: Verify midroll video ads for android games """
        assert self.page_ads_obj.verify_midroll_ads(self.obj, self.test_run_id, case_id) is True

    @pytest.mark.edge_windows_desktop
    @pytest.mark.chrome_windows_desktop
    @pytest.mark.safari_macOS_desktop
    @pytest.mark.chrome_macOS_desktop
    @pytest.mark.prod
    @pytest.mark.staging
    @pytest.mark.qa
    @pytest.mark.run(order=2510)
    def test_fredboat_utm_campaigns(self, case_id=8843490):
        """BERLIN::Ads --->C8843490: Verify no pre-roll ads for fredboat utm_campaigns """
        assert self.page_ads_obj.verify_no_preroll_ads_for_fredboat(self.obj, self.test_run_id, case_id) is True

    @pytest.mark.edge_windows_desktop
    @pytest.mark.chrome_windows_desktop
    @pytest.mark.safari_macOS_desktop
    @pytest.mark.chrome_macOS_desktop
    @pytest.mark.prod
    @pytest.mark.staging
    @pytest.mark.qa
    @pytest.mark.run(order=1102)
    def test_preloader_displayed(self, case_id=8843491):
        """BERLIN::Ads --->C8843491: Verify Preloader is displayed """
        assert self.page_ads_obj.verify_preloader_displayed(self.obj, self.test_run_id, case_id) is True


