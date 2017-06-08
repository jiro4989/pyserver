import os

def low2up(srcline):
	try:
		tmp = srcline.split("\t")
		if 0 < len(tmp):
			path = tmp[0]
			base = os.path.basename(path)
			base, ext = os.path.splitext(base)
			base = base.upper()\
			.replace("-", "_")\
			.replace("_COMPONENT", "")\
			.replace(".COMPONENT", "")
			result = "{base}_\t{srcline}".format(base=base, srcline=srcline)
			return result
	except Exception:
		return srcline
	else:
		return srcline

if __name__ == '__main__':
	pass
