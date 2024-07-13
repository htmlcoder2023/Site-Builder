import sys
company = input("Company: ")
open("script2.bat", "w")
file = open("script2.bat", "a+")
open("script_SET.bat", "w")
file2 = open("script_SET.bat", "a+")
gitUser = "git config --global user.name " + input("git config --global user.name: ")
gitEmail = "git config --global user.email " + input("git config --global user.email: ")
gitHost = "git clone " + input("git clone: ")
print("Paste the name of the git repository you just cloned. Otherwise, the script will not work properly.")
gitRepo = input("Name of Git Repository: ")
moveFILES = "move " + company + ".html " + gitRepo
moveDir_1 = "cd " + gitRepo
moveFILES_2 = "move " + company + ".html public"
mainBranch = "git switch --create master"
gitInit = "git init --initial-branch=master"
gitRemote = "git remote add origin " + gitHost.replace("git clone ", "")
moveDir_2 = "cd public"
endUser = "cd .."

file.write("\n" + gitUser)
file.write("\n" + gitEmail)
file.write("\n" + gitHost)
file.write("\n" + moveFILES)
file.write("\n" + moveDir_1)
file.write("\n" + moveFILES_2)
file.write("\n" + mainBranch)
file.write("\n" + gitInit)
file.write("\n" + gitRemote)
file.write("\n" + moveDir_2)
file.write("\n" + endUser)
file.write("\n" + endUser)

file2.write("script.py")
file2.write("\n" + "move " + company + ".html " + gitRepo)
file2.write("\n" + "cd nes-games-na")
file2.write("\n" + "move " + company + ".html public")
file2.write("\n" + "git add .")
file2.write("\n" + "git commit -m \"Update files\"")
file2.write("\n" + "git push --set-upstream origin master")
file2.write("\n" + endUser)

print("Program execution complete. Script2.py, script.bat and script2.bat will be deleted now.")
file.close()
file2.close()
sys.exit()