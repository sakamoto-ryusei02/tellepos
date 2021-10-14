import oseti

analyzer = oseti.Analyzer()
print(analyzer.count_polarity('私はとっても幸せ'))
print(analyzer.count_polarity('店員の態度は悪かったが、ここのラーメンはやばい'))
print(analyzer.count_polarity('遅刻したけど楽しかったし嬉しかった。すごく充実した！'))
