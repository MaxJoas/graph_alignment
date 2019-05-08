#https://rogerdudler.github.io/git-guide/index.de.html

git add <dateiname> #zum Index hinzufügen
git commit -m "Commit-Nachricht" #bestätigst deine Änderungen
git push origin master #änderungen hochladen

git pull origin master 

git pull #neuesten Änderungen zu aktualisieren
git fetch #Änderungen erst herunterzuladen
git merge #mit deinem Stand zusammenzuführen

git checkout -- <filename> #auf den letzten Stand im HEAD zurücksetzen
git fetch origin #lokale Änderungen komplett entfernen möchtest, holst du dir den letzten Stand vom entfernten Repository
git reset --hard origin/master

git config credential.helper store #zum Benutzernamen speichern
