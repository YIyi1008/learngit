#TestFixure_register.py
import unittest
from register import register


class TestFixure_register(unittest.TestCase):
	"""注册接口测试用例夹具的使用"""

	def setUp(self):
		#在每条测试用例执行前都会执行
		print("用例{}开始执行--".format(self))

	def tearDown(self):
		#在每条测试用例执行后都会执行
		print("用例{}执行结束--".format(self))

	@classmethod	#表示这个方法是以类为维度执行的

	def setUpClass(cls):
		#整个测试用例类中的用例执行之前执行此方法
		print("--setup--class------")

	@classmethod
	def tearDownClass(cls):
		#整个测试用例类中的用例执行 之后执行此方法
		print("--teardown--class")

	def test_register_success(self):
		"""注册成功"""
		data = ("testuser0","test000","test000")	#可以测试成功的数据
		expected = {"code": 1,"msg" : "注册成功"}	 #预期结果
		result = register(*data)	#将data中的数据传入导入的register函数
		self.assertEqual(expected,result)	#断言，判断实际结果和预期结果是否一致

	def test_register_isnull(self):
		"""注册失败，用户名为空"""
		data = ("","test123456","test123456")	#测试用户名为空的数据
		expected = {"code": 0,"msg" : "所有参数不能为空"}	 #预期结果
		result = register(*data)	#将data中的数据传入导入的register函数
		self.assertEqual(expected,result)	#断言，判断实际结果和预期结果是否一致



#要运行这个文件，需要unittest中的main函数来执行测试用例
if __name__ == '_main_':
	unittest.main()
