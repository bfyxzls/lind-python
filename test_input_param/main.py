from optparse import OptionParser
# 输入参数的使用
if __name__ == '__main__':
   parser = OptionParser()
   parser.add_option("--mode", dest="mode", help="interaction mode: training, test")
   (options, args) = parser.parse_args()
   print("Hello World",options.mode) # python main.py --mode=test
   if options.mode == 'training':
         print("training mode")
   else:
         print("test mode")
