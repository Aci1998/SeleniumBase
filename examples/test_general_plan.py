from utils.base_test_case import BaseTestCase

"""
计划管理
计划管理-普通计划
"""


class TestDistributionGeneralPlan(BaseTestCase):
    """
    python3 -m pytest test_case/one/test_general_plan.py
    """

    def test_add_regular_plan(self):
        """
        新建一个普通计划
        """
        self.login("DomainManager", "ac")

        self.click('//*[@id="menu-alIq_t8NvXM"]/span/span/span/span')
        self.click("//*[@id='driver-popover-item']/div[4]/button")
        self.click("//span[contains(text(),'新建普通计划')]")
        self.click("//span[contains(text(),'跳 过')]")

        self.click("//tbody/tr/td[1]/label[1]")
        self.click("//span[contains(text(),'下一步')]")
        self.input("//input[@placeholder='请输入1-50的整数']", '30')
        self.click("//span[contains(text(),'完 成')]")
