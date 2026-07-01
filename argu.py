def t_calc(bill_amount,tip_perc):
 t=bill_amount*(1+0.02*tip_perc)
 t=round(t,2)
 print(f" Please Pay ${t}")
t_calc(150,20)