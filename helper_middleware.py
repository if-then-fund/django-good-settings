class DumpErrorsToConsole:
	def process_exception(self, request, exception):
		import traceback
		print()
		print(request)
		print()
		traceback.print_exc()
		print()
		return None # let Django continue as normal
