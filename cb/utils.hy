;;;;
;;;;
;;;;


(import [debian.changelog [Changelog]])


(defn parse-changelog [filepath]
  (apply Changelog [] {"file" (open filepath "r")}))


(defn get-changelog [] (parse-changelog "debian/changelog"))


(defn get-latest-changes [] (. (get-changelog) _blocks [0]))
