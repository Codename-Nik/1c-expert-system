(deftemplate business
  (slot industry (type SYMBOL))

(deftemplate requirements
  (slot accounting (type BOOLEAN))
  (slot crm (type BOOLEAN))
  (slot payroll (type BOOLEAN)))

(defrule select-retail
  (business (industry retail))
  (requirements (accounting TRUE))
  =>
  (assert (recommendation "1С:Розница 8")))

(defrule select-manufacturing
  (business (industry manufacturing))
  (requirements (accounting TRUE))
  =>
  (assert (recommendation "1С:ERP 2.0")))