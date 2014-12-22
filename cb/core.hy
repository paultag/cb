;;;;
;;;;
;;;;


(import [cb.utils [get-latest-changes]])


(defn test []
  (let [[changelog (get-latest-changes)]]
    (import pdb) (.set-trace pdb)))
