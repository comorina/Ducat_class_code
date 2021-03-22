import pytube as pt
con=pt.YouTube("https://www.youtube.com/watch?v=7kn7NtlV6g0")
#print(con.streams)
con.streams[0].download()
print("done..")
