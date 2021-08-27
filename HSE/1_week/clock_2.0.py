sec = int(input())

print("%d:%02d:%02d"
      %(sec // 60 // 60 % 24,
      sec // 60 % 60,
      sec % 60))
