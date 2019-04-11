f = open('feedback.txt','r')
f1 = f.read()
cp=0
cneg=0
cneu=0
d={'positive':["excellent","good","brilliant"],
'negative':["horrible","worst","hated","bad"],'neutral':["ok","fine"]}
for line in f:
	word = line.split()
	if word == d['positive']:
		cp+=1
	if word == d['negative']:
		cneg+=1
	if word == d['neutral']:
		cneu+=1
f.close()
if cp>cneg and cp>cneu:
	print("Feedback is positive")
elif cneg>cp and cneg>cneu:
	print("Feedback is negative")
else:
	print("Feedback is neutral")