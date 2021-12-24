def compound_interest(p, t ,r):
    print(f"The principal is {p}")
    print(f"The time period is {t}")
    print(f"The interest rate is {r}")

    ci=p*(1+r/100)**t

    print(f"The compounded interest is {ci}")
    return ci
# test  & input
compound_interest(2500, 10, 5)
