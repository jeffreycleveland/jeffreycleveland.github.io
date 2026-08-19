# -*- coding: utf-8 -*-
"""Tidy long-format series assembled from the claims file: the subset that plots directly."""
import csv, os

OUT = os.path.dirname(os.path.abspath(__file__))
COLS = ["series_id","series_label","suggested_chart","region","unit","period","value","basis","claim_ids"]

R = []
def add(sid, label, chart, region, unit, points, basis="stated"):
    """basis: stated = the number appears in the book; derived = computed from a stated
    percentage change or ratio; assumed = an anchor the book does not give (see README)."""
    for period, value, cids in points:
        R.append([sid, label, chart, region, unit, period, value, basis, cids])

add("savings_rate","National savings rate, before and after the boom","slope","Britain","percent_of_gdp",
    [("1840s",8.5,"C008"),("1860s",13.5,"C008")])
add("savings_rate","National savings rate, before and after the boom","slope","Germany","percent_of_gdp",
    [("1840s",9,"C009"),("1860s",14,"C009")])
add("savings_rate","National savings rate, before and after the boom","slope","France","percent_of_gdp",
    [("1840s",17.5,"C010"),("1860s",19,"C010")])
add("savings_rate","National savings rate, before and after the boom","slope","United States","percent_of_gdp",
    [("1840s",15,"C011"),("1860s",20,"C011")])

add("exchange_size","Size of the three great exchanges on the eve of the crisis","bar","London","usd_million",
    [("1860s",12000,"C020")])
add("exchange_size","Size of the three great exchanges on the eve of the crisis","bar","Paris","usd_million",
    [("1860s",8000,"C021")])
add("exchange_size","Size of the three great exchanges on the eve of the crisis","bar","New York","usd_million",
    [("1860s",4000,"C019")])

add("boom_index","The first globalization, indexed to its starting point","line","Four major economies (GDP)","index_100",
    [("1848",100,"C002"),("1873",200,"C002")], basis="derived")
add("boom_index","The first globalization, indexed to its starting point","line","World trade volume","index_100",
    [("1848",100,"C003"),("1873",500,"C003")], basis="derived")
add("boom_index","The first globalization, indexed to its starting point","line","Global bond market","index_100",
    [("1850",100,"C004"),("1873",500,"C004")], basis="derived")
add("boom_index","The first globalization, indexed to its starting point","line","Bond market (London/Paris/NY)","index_100",
    [("1850",100,"C015"),("1870",600,"C015")], basis="derived")

add("growth_acceleration","Trend growth versus the final surge","slope","Industrial production, major powers","percent_per_year",
    [("1850s-60s trend",3.5,"C006"),("1872-73",7,"C006")])
add("growth_acceleration","Trend growth versus the final surge","slope","World trade","percent_per_year",
    [("1850s-60s trend",6,"C007"),("1872-73",10,"C007")])

add("real_rates","Long-term real interest rates in London","line","Britain","percent",
    [("pre-1840",6,"C012"),("1850s-60s",3,"C012")])

add("infra_investment","Global investment in railroads and infrastructure","bar","World","usd_million_per_year",
    [("early 1850s",1000,"C013"),("late 1860s",4000,"C013")])

add("bubble_run_up","Anatomy of four bubbles: run-up and collapse","line","Dutch tulips (1636-37)","index_peak_100",
    [("peak minus 3m",5,"C022"),("peak",100,"C022"),("peak plus weeks",5,"C023")], basis="derived")
add("bubble_run_up","Anatomy of four bubbles: run-up and collapse","line","British railway shares (1844-48)","index_peak_100",
    [("1844",50,"C024"),("1845 peak",100,"C024"),("1848",40,"C025")], basis="derived")
add("bubble_run_up","Anatomy of four bubbles: run-up and collapse","line","Vienna listed stocks (1870-73)","index_peak_100",
    [("1870",25,"C039"),("1873 peak",100,"C039"),("1873-05-09",55,"C045")], basis="derived")
add("bubble_run_up","Anatomy of four bubbles: run-up and collapse","line","Berlin large caps (1870-72)","index_peak_100",
    [("1870",50,"C035"),("1872 peak",100,"C035")], basis="derived")

add("vienna_land","Viennese land prices, pre-boom versus peak","dumbbell","Vienna, low end","usd_per_sq_ft",
    [("pre-boom",2,"C041"),("1873 peak",10,"C041")])
add("vienna_land","Viennese land prices, pre-boom versus peak","dumbbell","Vienna, high end","usd_per_sq_ft",
    [("pre-boom",3,"C042"),("1873 peak",20,"C042")])
add("vienna_land","Viennese land prices, pre-boom versus peak","dumbbell","Vienna, small central tract","usd",
    [("pre-boom",5000,"C043"),("1873 peak",70000,"C043")])

add("german_float","The Gruenderjahre: companies founded on the indemnity","bar","Germany, all new companies","count",
    [("1871-73",850,"C032")])
add("german_float","The Gruenderjahre: companies founded on the indemnity","bar","Germany, floated in Berlin","count",
    [("1871-73",450,"C033")])

add("panic_1873_stocks","Bellwether stocks through the Panic of 1873","line","Western Union","usd_per_share",
    [("1873-09 pre-panic",92,"C059"),("1873-11",46,"C059")])
add("panic_1873_stocks","Bellwether stocks through the Panic of 1873","line","New York Central","usd_per_share",
    [("1873-09 pre-panic",105,"C060"),("1873-11",83,"C060")])
add("panic_1873_stocks","Bellwether stocks through the Panic of 1873","line","Union Pacific","usd_per_share",
    [("1873-09 pre-panic",27,"C061"),("1873-11",16,"C061")])

add("rr_bond_default","Default rate on U.S. listed railway bonds","area","United States","percent_of_2200m_outstanding",
    [("1873",0,"C046"),("1875-12",33,"C050"),("1878",50,"C047")], basis="derived")

add("price_level","The great deflation, 1873 = 100","line","Britain and United States (CPI)","index_1873_100",
    [("1873",100,"C068"),("1880",85,"C068"),("1896",67,"C070")], basis="derived")
add("price_level","The great deflation, 1873 = 100","line","World (all prices)","index_1873_100",
    [("1873",100,"C066"),("1879",77.5,"C066")], basis="derived")
add("price_level","The great deflation, 1873 = 100","line","United States (wholesale)","index_1873_100",
    [("1873",100,"C067"),("1879",65,"C067")], basis="derived")

add("silver_price","The price of silver after demonetization","line","World","usd_per_ounce",
    [("1872",1.32,"C071"),("1892",0.83,"C071")])

add("uk_capital_outflows","British capital exports around the crisis","line","Britain","usd_million_per_year",
    [("1872",500,"C079"),("1878",100,"C080"),("1888",500,"C081")])

add("equity_returns","Real equity returns, quarter century before and after 1873","dumbbell","Britain","percent_per_year",
    [("1848-1873",13,"C103"),("1873-1898",5,"C103")])
add("equity_returns","Real equity returns, quarter century before and after 1873","dumbbell","United States","percent_per_year",
    [("1848-1873",11,"C104"),("1873-1898",7,"C104")])

add("transport_costs","The other deflation: collapsing freight costs","dumbbell","Grain, Chicago to New York (rail)","cents_per_bushel",
    [("1870",30,"C114"),("early 1890s",13,"C114")])
add("transport_costs","The other deflation: collapsing freight costs","dumbbell","Grain, transatlantic","cents_per_bushel",
    [("1870",20,"C115"),("early 1890s",2,"C115")])

add("tariffs_manufactures","Europe abandons free trade","line","Europe, manufactured goods","percent",
    [("1850",28,"C131"),("early 1870s",8,"C131"),("1890s",17.5,"C132")])
add("tariffs_manufactures","Europe abandons free trade","line","United States, manufactured goods","percent",
    [("1850",40,"C133"),("early 1870s",40,"C133"),("1890",50,"C134")], basis="assumed")
add("tariffs_grain","Grain tariffs after the price collapse","dumbbell","Germany","percent",
    [("1870s",6,"C129"),("1890s",30,"C129")])
add("tariffs_grain","Grain tariffs after the price collapse","dumbbell","France","percent",
    [("1890s",40,"C130")])  # the book does not give France's pre-tariff level

add("egypt_debt","Egypt's debt stack at the moment of default","stacked_bar","Bonded debt (mostly British holders)","usd_million",
    [("1876",350,"C084")])
add("egypt_debt","Egypt's debt stack at the moment of default","stacked_bar","Floating-rate debt (mostly French holders)","usd_million",
    [("1876",100,"C085")])
add("egypt_debt","Egypt's debt stack at the moment of default","stacked_bar","Arrears to contractors and civil servants","usd_million",
    [("1876",50,"C086")])

add("rothschild_scale","The House of Rothschild, capital and profits","line","Bank capital","usd_million",
    [("1815",10,"C092"),("1850",40,"C094"),("1867",150,"C094"),("1870",200,"C096")])
add("rothschild_scale","The House of Rothschild, capital and profits","line","Annual profits","usd_million",
    [("1850",1,"C093"),("1867",6,"C093"),("1880-1900 avg",7,"C099")])
add("bank_capital_1865","Bank capital on the eve of the crisis","bar","Rothschild (four houses)","usd_million",
    [("1865",150,"C094")])
add("bank_capital_1865","Bank capital on the eve of the crisis","bar","Baring Brothers","usd_million",
    [("1865",15,"C100")])
add("bank_capital_1865","Bank capital on the eve of the crisis","bar","Jay Cooke & Co.","usd_million",
    [("1865",10,"C054")])

add("then_and_now","The book's own 1873-2026 comparison (1,200x deflator)","bar","U.S. railway bonds, annual issuance","usd_million",
    [("early 1870s, nominal",500,"C150")])
add("then_and_now","The book's own 1873-2026 comparison (1,200x deflator)","bar","Same, in 2026 dollars","usd_million_2026",
    [("early 1870s, restated",600000,"C151")])
add("then_and_now","The book's own 1873-2026 comparison (1,200x deflator)","bar","Projected major-tech capex","usd_million_2026",
    [("2026",600000,"C152")])

with open(os.path.join(OUT, "series.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(COLS)
    w.writerows(R)

print("rows:", len(R), "series:", len({r[0] for r in R}))
