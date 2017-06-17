# Finance for Non-Finance Professionals

https://www.coursera.org/learn/finance-for-non-finance/home/welcome

## WEEK 1: BASIC PRINCIPLES OF FINANCIAL VALUATION DISCOUNTING

### Lectures

Going to learn:
- Interest rates
- Compound rate of return
- Discounting the future
- Financial valuation by **DCF**
- Ratio Analysis
- Examples and Applcations

Human Nature and the Time Value of Money

*Time Value of Money*
- which is preferred: $100 today or $100 5 years from now

*Opportunity Cost*

*Inflation*

*Risk*

*Interest Rate*

Changes in Interest Rate due to e.g.
- **opportunity cost** ie better economic growth
- **inflation** ie govt prints more money
- **risk** ie wars, disasters, etc

Interest rates in the economy
- the most important price in the economy
- the price of time
- the basis for all other prices

Compounding and Earning Returns Over Time

*Compounding*

e.g
- interest = 11%
- $100 in 5 years

    year  | Amount
    ---------------
    0     | 1000
    1     | 1110
    2     | 1232
    3     | 1368
    4     | 1518
    5     | 1685

Compounding interest grows faster than simple interests

*FV = PV * (1 + r)^t*

      FV= Future Value
      PV = Present Value
      r = interest rate
      t = time

    r = t√( FV / PV ) - 1

Discounting Future Cash Back to the Present

*Discounting* := what is a cash flow in the future worth today?

           FV
    PV = --------
         (1+r)^t

If I offered you $175 payable 5 yrs from now, how much would you pay for that
offer today if interest rates were 4%

    PV = 175 / (1 + 4%)^5 = 143.84

Discount decays exponentially ie longer t => much lower PV

e.g. friend wants to borrow $1000 over 7 years.
- assume market at 5% interest compound annual

    PV = 1000 / (1 + 5%)^7 = $710.70

i.e I would be willing to loan $710.70 with expectation of getting paid back
$1000 in 7 years

e.g. if i think business is even riskier, i might discount at 15%

    PV = 1000 / (1 + 15%)^7 = 375.90

ie the higher risk => greater discount => loan out less money

Discounted Cash Flow (DCF) as the Basis for All Valuation

*DCF*
- method of valuing investment
- uses all anticipated future cash flows
- discounts all cash flows back to present value

Investing => earn a return

Knowing the following two we can value anything
- how much cash will come in
- when will cash come in

*Bond*
- contract between an insurer and bondholder
- buyer of bond lends money to issuer
- issuer pays interest on loan
- issuer repays principal at maturity

e.g. Simple bond of $3000 with annual payments of $250 for 5 yrs at discount
rate of 7%. What is it worth?
- Step 1: what are the cash flows
- Step 2: What are they worth today?
- Step 3: Add up the present values

    yr     | 0 |  1    |  2    |  3    |  4    |  5       | total
    -------------------------------------------------------------
    return |   | 250   | 250   | 250   | 250   | 250 + 3k | 4250
    -------------------------------------------------------------
    discnt |   | 233.6 | 218.4 | 204.1 | 190.7 | 2317.2   | 3164

The 3k bond is worth $3164 if sold today

e.g. Bond pays $1k in 2 years with a coupon of $50/yr. Assuming discounted rate of 5% what is the price?

    1000/(1.05)^2 + 50/(1.05)^2 + 50/(1.05)^1 = 1000

*DCF applies to any asset with cash flow*
- Stock Valuation
- real estate
- mergers and acquisitions
- derivatives

*Cash and timing drive all valuation*

*DCF Practical Example*

Water well in the deser. How much is it worth to sell or acquire?
- if the well is dry
- connected to water source

value drivers
- how much waters e.g. infinite
- produced 1 gallon/day
- how much cash flow = net $1.50/day

      0   1     2     3     4     5     ...   infinity
          1.50  1.50  1.50  1.50  1.50  ...

Assume Discount rate = 15%

Build a [Spreadsheed model "Water Well Valuation Example"](https://docs.google.com/spreadsheets/d/17Rim9Xqg8QYluO3HxvsRvQ75nU30Jb0TrCrlIEMxm4s/edit?usp=sharing)
- Note that at year 18 PV is less than $100
- Note that PV approaches 0 pretty fast
- Note the graph of PV over time exponentially goes down

*Note* PV in year 20 is less than year 2. As r goes up, PV goes down

*Increasing risk increases the discount rate and decreases PV*

Valuation by Comparables

*comps* = Comparables

Comparable transactions or prices

Quick, easy, and **dangerous!**

Less accurate than DCF, used for quick back of envelope calculations

Assumptions for Comps
- you can identify close comparables
- you have a value-relevant ratio e.g. price to earning ratio
- the market values comps similarly

*(Price / Attribute) * Your Attribute = Price of Asset*

Examples of attributes
- P/E ratio
- Earnings yield
- Divedend yield
- Return on Assets
- EBITDA multiples

*P/E Ratios*
- "Trades at X times earnings"

Example: Value Lowes Corporatoin by Comps
- Comp to Home Depot

                  Home Depot    Lowes
    ----------------------------------
    Price (stock) 170           74
    (E)arnings    $6.80         $2.46
    P/E           25
    ----------------------------------
    Comp Value                 $61.60

    Comp value of Lowes = P/E (Home Depot) * E (Lowes)
                        = 25 * $2.46 = $61.60

Assuming lowes trades at $74/share, there is a 20% difference in market price to comp
- **Be careful if you see a large diff between comp and market price**

Other common Comps
- Return on Assets or Equity (ROA/ROE)
- Return on invested capital (ROI)
- Dividend yield
- PEG ratio (PE ratio over Growth in E)

Measuring Comps
- rely on historical averages
- ad-hoc time e.g. 12months or 3 years
- negative earnings, negative prices?

Comps vs DCF
- both provide useful information
- Comp for ballpark
- DCF for more accurate analysis
- Both require forecasts
- DCF more accurate but requires more work

Examples and Applications: Bonds


*BONDS*

- Simple debt instruments
- Promise coupons (interest) and face value
- Easy application of DCF valuation

*KINDS OF BONDS*

- U.S. treasury bonds
- Corporate Bonds
- Municipals
- Sovereign Debt

What’s different about each?
- risk in buying Greek govt vs Cleveland school district

*HOW TO VALUE BONDS*

- Bond contract: what cash and when
- All we need to do is discount the payments

*TREASURY BOND EXAMPLE*

Treasury issues 3 year bonds with a 2.5% coupon rate.  If the six month interest rate is 1.2%, what is the price of the bond per $100 of face value?

    Time = 6 months
    CR annual = 2.5%
    CR semi-annual = 1.25%

    FV = $100
    T = 3 years = 6 semi-annual blocks
    r = 1.2%

        0   | 1    | 2    | 3    | 4    | 5    | 6            | Calculation
    return  | 1.25 | 1.25 | 1.25 | 1.25 | 1.25 | 1.25 + 100   | F * CR
    PV      | 1.24 | 1.22 | 1.21 | 1.19 | 1.18 | 1.16 + 93.09 | Ret / (1 + r)^t

    PV = Sum(PV) = 100.29 Present value of the bond

Examples and Applications: Mortgages


*MORTGAGES*
- Simple debt instrument
- Borrow money today to purchase real estate
- Each payment includes principal and interest
- Amortization schedule: what you're paying in interest vs principal

*MORTGAGE EXAMPLE Problem: Assume a bank charges 7% interest per year.  You*
borrow $10,000 to be repaid in equal yearly installments of $3,810.52 over 3
years.  Let’s amortize the loan schedule and compute interest and principle
repayments.

    Yr | Payment    | Interest | Princ Pymt | Balance   | Formulas
    -------------------------------------------------------------
    0  | --         | --       | --         | $10,000   | Interest = Balance * 7%
    1  | $3,810.52  | $700.00  | $3,110.52  | $6,889.48 | Princ = Payment - Interest
    2  | $3,810.52  | $482.26  | $3,328.26  | $3,561.22 |
    3  | $3,810.52  | $249.29  | $3,561.22  | 0         |



Examples and Applications: Annuities


*ANNUITIES = Series of equal payments at regular intervals. *
- Regular deposits to savings account
- Monthly mortgage payments
- Insurance premiums
- Pension payments

*RETIREMENT ANNUITY EXAMPLE: You want to retire and maintain a monthly income of*
$2,500 for the next 20 years.  How much would it cost to purchase this annuity
if discount rates are currently 4%?

*NOTE: If an annuity is 15% annual compounded monthly then*
`monthly interest rate = (1 + r)^(1/12) - 1`

[Annuities Example](https://docs.google.com/spreadsheets/d/1G1PWrHOVmnjHSdKdWxQ0Yh2VxbQRZK9U9HPhEY3bx9o/edit?usp=sharing)

Examples and Applications: Capstone Example

[Capstone Example XLSX for calculations](https://docs.google.com/spreadsheets/d/1Lu9qF-dY0DG2Udbh6GG78ERedHN6TjEysLTxqddUwCk/edit?usp=sharing)

*USING COMPOUNDING AND DISCOUNTING TO MAKE DECISIONS*
- You have a choice between three options:
  1. Take $1,000 in cash now
  2. Receive $2,000 at the end of three years
  3. Wait 10 years to receive $3,000
- Which is best choice if discount rate is 10%? `Option 2` since it has the highest PV
- How does the answer change if r = 5%? `option 3`

As discount rate goes down, we can be more patient (longer term option is
better).

*Discount rate => how much risk you're accepting*

### Finance in the Field

*CONVERSATION WITH CHRISTINE BOYD, CORPORATE FINANCE.*

What kind of valuation techniques do you uise in the field?
- Use all comps, ratios, and DCF and set a weighting method
- DCF has highest weight
- Wall St also uses all 3 methods
- Typical corporate finance depts aren't as sophisticated so using comps is easier to communicate
-

Discussion Prompt: Real World Application: Introduce Yourself!

### Assignment

Practice Quiz: Homework Assignment

*1 If the annual interest rate is 15%, would you rather have:*
  - 800 now
  - ✓ $$3,500 at the end of 10 years

    FV = PV / (1 + r)^t

    FV = 3500, r = 0.15, t = 10
    3500 / (1 + 0.15)^10 =

*2 For the same problem, would you rather have:*
  - 800 now
  - ✓ $3,500 at the end of 10 years, compounded quarterly

    PV = FV / (1 + r/n)^(n*t)

*3 If you invest $1,000 in a bank paying an annual interest rate of 10%, how
long would it take to double the initial investment?*
  - 2 years
  - ✓ 7.27 years
  - 6.66 years

    FV = PV * (1 + r)^t

    2000 = 1000 * (1 + 10%)^t

    2 = 1.1^t

    log(2) 1.1 = t

    t ~= 7

*4 Suppose you put $1,000 into a bank account with an interest rate of 5%. What
will be the account balance at the end of 10 years if the interest is
compounded monthly?*
  - ✓ $1,647
  - $1,639
  - $1,629

     1647 = 1000 * (1 + 0.05/12)^(12*10)

*5 For the same problem, what will be the account balance at the end of 10
years if the interest is compounded quarterly?*
  - $1,647
  - ✓ $1,644
  - $1,639

    1644 = 1000 * (1 + 0.05/4)^(4*10)

*6 For the same problem, what will be the account balance at the end of 10
years if the interest is compounded daily?*
  - ✓ $1,649
  - $1,500
  - $1,650

    1649 = 1000 * (1 + 0.05/365)^(365*10)

*7 What is the present value of a simple bond with face value of $2,000 that
makes annual payments of $200 for 3 years at a discount rate of 5%?*
  - $1,900.44
  - ✓ $2,272.33
  - $2,600.00

[Sheet 2](https://docs.google.com/spreadsheets/d/1wcnsowb7NDrOF0Zs9a5mCGxLdx_7iTuPnVoqfR5Elu8/edit?usp=sharing)


    = ( SUM[i=1, 3](200 / (1 + 0.05)^i) ) + ( 2000 / (1 + 0.05)^3 )


    Year  CF    PV[CF]
    1     200   190.48
    2     200   181.41
    3     200   172.77
                ------
                544.65

    = 544.65 + 1727.68 = 2272.32

*8 A bond with a face value of $10,000 that makes annual payments of $200 for 5
years at a discount rate of 3% is being offered for $9,000 today. Is this a
profitable bond?*
  - ✓ yes
  - no

[Sheet 2 2nd table](https://docs.google.com/spreadsheets/d/1wcnsowb7NDrOF0Zs9a5mCGxLdx_7iTuPnVoqfR5Elu8/edit?usp=sharing)

    Total = 9554.32

*9 How much would you be willing to pay for a bond with a face value of $4,000
that makes annual payments of $500 for 3 years at a discount rate of 6%?*
  - $4,133
  - ✓ $4,695
  - $5,500

[Sheet 2 2nd table](https://docs.google.com/spreadsheets/d/1wcnsowb7NDrOF0Zs9a5mCGxLdx_7iTuPnVoqfR5Elu8/edit?usp=sharing)

*10 Company A is earning $2.46 per share and currently trading at $10 per
share.  Comparable Company B is trading at $24 per share and a P/E ratio of 4.6
with earnings of $1.33 per share. Using a P/E ratio valuation, would you buy
shares in Company A?*
  - ✓ yes
  - no

    E[A] = 2.46
    Price[A]= 10

    Price[B] = 24
    PE[B] = 4.6
    E[B] = 1.33

    Comp value  of A = PE(B) * E(A)
      = 4.6 * 2.46 = 11.316

    Comp Value of $11.316 is greater than the 10/share it's trading at.


*Do I not understand P/E? How is Company P/E = 4.6 when P = 24 and E = 1.33?*

### Quiz: Week 1 Quiz

1 What are the 3 main factors that affect Interest Rates?
- War, Recession, Timing
- Opportunity Costs, Inflation, Risk
- Economic Conditions, Historical Price Trends, Stock Market

2 Choose between these prizes if the interest rate is 10%:
- $1,000 now
- $1,500 at the end of 4 years

3 If you need $20,000 for a car purchase by the time you graduate from college
in 4 years and interest rates are 2%, how much would you need to put into
savings today?
- $9.645.06
- $10,204.08
- $18,476.91
- $18,491.12

4 What happens to the present value of $1,000 when the due date that it is to
be paid changes from 5 years to 4 years?
- PV goes up
- PV goes down

5 Suppose you put $1,000 into a bank account that pays an annual interest rate
of 5%. What will be the account balance at the end of 10 years? Assume there is
no deposit or withdrawal in the interim.
- $1,000
- $1,500
- $1,628.90
- $1,436.70

6 In the above bank account, what would the account balance be at the end of 10
years if the interest rate is compounded semi-annually?
- $1,638.62
- $1,628.90
- $1,500.00

7 What is the present value of a simple bond that costs $6,000 and makes annual
payments of $300 for 5 years at a discount rate of 3%?
- $5,434.44
- $6,549.56
- $7,500.00

8 What is the value of a share of stock in Company A that is earning $1.57 per
share using a P/E ratio valuation to comparable Company B trading at $15 and a
P/E ratio of 14 with earnings of $2.42 per share?
- $21.98
- $23.55
- $33.88

9 Suppose a bond will pay $1,000 in 2 years. At the end of each of the next 2
years, the bond will also pay a coupon of $50. Assume a discount rate of 10%.
What is the price of this bond?
- $900
- $913.22
- $1000
- $1012.51

10 For the same bond, suppose the discount rate is 3%. What is the price?
- $976.21
- $1,000
- $1,012.51
- $1,038.27



## WEEK 2: HOW TO SPEND MONEY MONEY (CAPITAL BUDGETING TOOLS)

### WEEK 2 OVERVIEW

- Capital budgeting process
- NPV - Net Present Value
- Payback period
- Accounting ratios
- IRR - Internal rate of return
- Putting it all together

### OVERVIEW OF THE CAPITAL BUDGETING PROCESS

                Buy Assets             Raise Cash
                   <---                   <---
    {Firm's Assets}    {Financial Manager}    {Financial Markets}
       ↑           --->         |         --->
       |         Cash Flow      |        Payout
       |                        |
       ------ Reinvest ----------

- You have to pay for other peoples money
- Implicitly, you pay them **r** (interest)

Capital Budgeting = How should we decide the how, when, and where of how to spend money?

Similar to an individual investor:
1.  Timing - when do I get my money back
2.  Risk - what is the risk
3.  Opportunity Cost - I need car instead

*Risk vs. Return over time*

*BEST PRACTICES*
- Arms-length => no inside dealing e.g. giving money to relative
- Objective => borrower and borrowee can agree
- Transparent => can report to auditing

*CAPITAL BUDJETING*
- Accept or reject
- Best of a set
- Rank different projects

Cost/Benefit analysis: When are benefits > cost

In Review
- Review tools
- Understand tradeoffs
- Metrics in perspective
- Sensitivity analysis
- Putting it all together

### NPV - NET PRESENT VALUE

1. Add up the PV of all future cash
2. Compare with initial investment

Decision rule **Invest if NPV > 0**
- i.e. Benefit > Cost

*NPV Formula: -(Initial Cost) + SUM[CF(n) / 1 + r)^n]*
- where CF = Cash Flow
- n = period
- r = interest

    NPV = -(Initial Cost) + ( CF₁ / (1+r)^1 ) +  ( CF2/ (1+r)^2 ) +

*Initial investment vs Positive future cash flow*

Problem: Analyze the table of cash flows and compute the NPV if the discount
rate is 10%?

    Period | Cash Flow | Present Value
    ----------------------------------
         0 | -1500     | -1500
         1 |   900     |   818.18
         2 |   750     |   619.83
    ----------------------------------
     Total |  $150     |  -$61.98

The Cash Flow every period needs to be discounted. Hence the NPV is less than the CF

    NPV => Discounted Cash Flow

*QN: What is the NPV of a project that requires an initial outlay of $1000 and provides an annual income of $500 for 3 years? Assume a discount rate of 5% and each annual income is paid at the end of the year*
- ✓  361.62
- 450.70
- 205.19
- 356.60

https://docs.google.com/spreadsheets/d/1Qf1D1R1pj0f10-HQ6Oe6KZrl0uFHec5v4hudLjKYvos/edit?usp=sharing

Main Drivers
- Cash flow (more is better!)
- Timing (the sooner the better)
- Discount rate (lower the better)

Wrap Up
- NPV is the Best capital budgeting tool
- Incorporates:
  - Timing
  - Opportunity cost
  - Risk
- Objective
- Arms-length
- Transparent

### PAYBACK PERIOD

How long it takes to earn back initial investment?

Decision rule **Invest if payback is less than X**

*PAYBACK PERIOD: EXAMPLE*

    Project | Cash Flow               | Payback
    -------------------------------------------
            | 0    | 1   | 2   | 3    |
    ------------------------------------------
        X   | -500 | 500 | 250 | $0   | 1
        Y   | -500 | 100 | 200 | $600 | 3
        Z   | -500 | 300 | 400 | $400 | 1.5

- For Proj X I get my money back in first year
- For Proj Y It takes year 3 to get back initial $500
- For Proj Z It takes year 1.5 to get back initial $500

ie Project X is best since I get my money back fastest

The good:
- Time is money!
- Reflects the opportunity cost

The bad:
- Neglects cash after the payback. ie. might turn into a cash cow after the
  initial payback period
- Neglects timing
- Neglects risk
- Arbitrary cut off

*PAYBACK VS NPV *

    Project | Cash Flow                  | Payback | NPV (10%)
    ----------------------------------------------------------
            | 0     | 1    | 2    | 3    |         |
    ----------------------------------------------------------
        X   | -$500 | $500 | $250 | $0   | 1       | 161
        Y   | -$500 | $100 | $200 | $600 | 3       | 207
        Z   | -$500 | $300 | $400 | $400 | 1.5     | 404

*Even though Proj X gets paid back fastest it has the lowest NPV.*

*QN: A project requires an initial investment of 2k upfront. I will produce an annual income of 1k every year for 3 years with discount rate of 10%. What is the payback period?*
- ✓ 2.352
- 2.000
- 1.579
- 2.775

https://docs.google.com/spreadsheets/d/1Qf1D1R1pj0f10-HQ6Oe6KZrl0uFHec5v4hudLjKYvos/edit?usp=sharing


*PAYBACK WRAP-UP*

- Often a weak capital budgeting tool
- Accept projects where Payback < X
- Measures time to recovery
- Arbitrary, no risk or timing, ad hoc

### ACCOUNTING RATIOS

Measure the ratio of `A/B`

Decision rule: **Invest if the ratio > X**

*PAYBACK PERIOD: ROIC*

*ROIC* = return on invested capital

Decision rule: **Invest if ROIC > X**

*ROIC: EXAMPLE*

                 Year | 0    | 1    | 2    | 3
    ----------------------------------------------
    Book investment   | -450 | -300 | -150 |    0
    Revenue           |      |  600 |  500 |  400
    Cash outflows     |      | -300 | -250 | -200
    Depreciation      |      |  150 |  150 |  150
    ----------------------------------------------
    Accounting Profit |      |  150 |  100 |   50

*Cash Outflow* = Cost to generate the revenue for the year

*Depreciation* = reduction in value of the asset every year

*Account profit* = Revenue - Cash outflow - Depreciation

    Average profit = (150 + 100 + 50) / 3 = 100

    IC (Invested capital) = (450 + 300 + 150 + 0) / 4 = 225

    ROIC = Average profit / Average IC = 100/225 = 44%

*OTHER ACCOUNTING RATIOS we could have used*
- Return on assets (ROA)
- Return on equity (ROE)
- Gross margin (Gross Profit/Sales)
- Profit margin (Net profit/Net Sales)
- Profitability index

*QN: What is the ROI of a project that requires investments of 500 in each of the first 3 years and yields an income of 100, 75, and 50?*
- ✓ 15%
- 20%
- 10%

*ACCOUNTING RATIOS*

The good:
- More money is better!
- Reflects the use of capital

The bad:
- Neglects timing
- Includes accounting distortions - e.g. depreciation is an accounting artefact, not actual cash paid out
- Neglects risk
- Arbitrary cut off

*ACCOUNTING RATIOS: WRAP-UP*

- Accept projects where Ratio < X
- Weak capital budgeting tool
- Arbitrary, no risk or timing, ad hoc
- Not focused on cash creation

### IRR - INTERNAL RATE OF RETURN

i.e. **What discount rate makes NPV = 0?**
- A measure of the resiliency of the cash flow

Decision rule: **Invest if that rate > r**

*IRR*

- Discounting more drives NPV down
- How hard can NPV get hit and stay > 0
- **This decision rule is similar to NPV**

- NPV is a number that can be hard to internalize.
- IRR gives you a % that is more intuitive

*QN: Company XYZ is considering an investment that requires an initial outlay
of 500M and yields an income of 505M in a year. Should this project be accepted
if the company requires a discount rate of 10%?*
- No. 505 / (1 + 10%) = 459.10 which is less than 500

*IRR VS NPV FORMULA*

    NPV = -(IC) + SUM[CF(n) / (1+r)^n]
        = -IC + SUM[CF(n) / (1 + IRR)]

This is easier to do with a spreadsheet

*IRR: RELATION TO NPV RULE - Example graph of NPV v Discount Rate*

    NPV
     |
     *
     |*
     | *
     |   *
     |      *
     |----------*-------- Discount rate
     |              *
     |                   *

*IRR: EXAMPLE (TRIAL AND ERROR)*

    Time | Cash Flow | Trial 1 (10%) | Trial 2 (20%) | Trial 3 (16%)
    ----------------------------------------------------------------
       0 |  (9364)   | (9364)        | (9364)        | (9364)
       1 |  10000    |  9091         |  8333         |  8621
       2 |   1000    |   826         |   694         |   743
    ----------------------------------------------------------------
     NPV |   1636    |   553         |  -336         |     0

i.e. IRR = 0 was somewhere between 10% and 20%

*QN: What is the IRR of a project that requires an initial outlay of 15,220 and inflows of 5k, 6k, and 7k at end of each of the first 3 years?*
- 8.38

https://docs.google.com/spreadsheets/d/1Qf1D1R1pj0f10-HQ6Oe6KZrl0uFHec5v4hudLjKYvos/edit?usp=sharing

*IRR EXAMPLE IN SPREADSHEET*

Excel has an IRR function

    =IRR(B4:B6)

[Example of IRR Function in Excel](https://docs.google.com/spreadsheets/d/1Qf1D1R1pj0f10-HQ6Oe6KZrl0uFHec5v4hudLjKYvos/edit?usp=sharing)

*INTERNAL RATE OF RETURN*

- Similar to NPV
- Scales NPV into a %
- More intuitive
- Accounts for timing, opportunity cost, and risk

*INTERNAL RATE OF RETURN: WRAP-UP*

- Accept projects where IRR > r
- Good capital budgeting tool
- Accounts for risk, timing, and opportunity
- Loses the scale

### WRINKLES WITH IRR

Be careful; Not ideal for
1. Loan-type flows; where money is coming in and out
2. Scale problems; hard to know how much we're making overall
3. Timing problems
4. No IRR or multiple IRRs

*IRR WITH LOAN-TYPE FLOWS issues*
- When the cash flows are reversed => misleading what cash flow is
- Money in, then money out - Any time the signs flip

*IRR WITH LOAN-TYPE FLOWS: EXAMPLE*

    Project | CF₀   | CF₁   | IRR | NPV at 10%
    ------------------------------------------
        X   | (400) |  500  | 25% |  54.54
        Y   |  400  | (500) | 25% | (54.54)

In both cases the IRR is the same even though we flipped the order in which the
money came in and out. Note the NPV is -ve in 2nd case

*QN: What is the IRR of an investment that requires 1k upfront and pays 50 at end of first 2 years and additional lump sum of 1k at end of year 2?*
- [5%](https://docs.google.com/spreadsheets/d/1Qf1D1R1pj0f10-HQ6Oe6KZrl0uFHec5v4hudLjKYvos/edit?usp=sharing)


*IRR WITH LOAN-TYPE FLOWS*

![NPV vs IRR](https://drive.google.com/uc?id=0BwjXv3TJiWYEZ0xnTjkzRjVOdms)

This image shows where the 2nd line has a -ve NPV evern though the IRR is the same


*COMPARING SCALE WITH IRR *
- Hard to compare mutually exclusive projects
- Higher IRR might now imply higher NPV

*COMPARING SCALE WITH IRR*

    Project | CF₀   | CF₁   | IRR  | NPV at 10%
    -------------------------------------------
        X   |  -1   |   2   | 100% | 0.82
        Y   | -100  | 120   |  20% | 9.1

Project X is a rig that cost $1 but generated $2. For Y I could have moved the same rig at higher cost with greater return. IRR for X looks higher but NPV shows that Y has much better returns


*MULTIPLE OR NO IRR*
- There could be no rate that sets NPV = 0
- Different rates might set NPV = 0

*COMPARING SCALE WITH IRR*

    Project | CF₀  | CF₁ | CF₁   | IRR
    ----------------------------------------
        X   | -100 | 235 | 136.5 | [5%, 30%]
        Y   | -100 | 120 | -50   | --

![In Project X, IRR has 2 values and in Proj Y there is no IRR.](https://drive.google.com/uc?id=0BwjXv3TJiWYEWEV5aHJucTJZSTA)

*WRINKLES WITH IRR: WRAP-UP*
- Be careful!
- Always check for sign changes
- Always check for multiples
- Always compare with NPV!

### USING ALL THE METRICS TOGETHER

Most CFOs rely on multiple metrics. Study below shows what how much CFOs depend
on each metric.

    Internal Rate of Return (IRR) |======== 76
          Net Present Calue (NPV) |======== 75
                   Payback Period |====== 57
         Earnings Mulitples (P/E) |==== 39
               Discounted Payback |=== 30
        Accounting Rate of Return |== 20
              Profitability Index |= 12

          Source: John Graham and Campbell Harvey, 2001

*QN: What should be the objective of management?*
- maximize salary
- ✓ maximize shareholder value
- maximize earings
- minimize cost

*PUTTING ALL THE METRICS TOGETHER*
- NPV always first best approach
- IRR puts NPV in perspective
- Payback can be useful
- Ratios are informative and easy
- There should be a consistent theme


### SENSITIVITY ANALYSIS

*THE MAIN CAPITAL BUDGETING TOOLS*
1. NPV
2. IRR
3. Accounting Ratios
4. Payback

*CASH FLOW FORECASTING*
- Everything depends on forecasts; pretend we know how much it will project
  will cost, return, etc
- All forecasts are wrong! Have to be comfortable with this. Just because we
  can't forecast perfectly doesn't mean we shouldn't do it
- How sensitive are our decisions?
- What are the main value drivers?

*QN: What is the most relevant measure of how much cash a project is generating?*
- Depreciation
- Initial investment
- ✓ Free cash flows
- Sales

*SCENARIO ANALYSIS*

        Time | Cash Flows (Expected)
    --------------------------------
           0 | -$5000
           1 | -$3200
           2 |  $2500
           3 |  $1200
           4 |  $1200
           5 |  $1200
    --------------------------------
    NPV @15% |  $1745

If we're not comfortable with the expected forecast, we can break it down into
*pessimistic*, *expected*, and *optimistic*.

    Time     |              Cash Flows
             | Pessimistic | Expected | Optimistic
    ----------------------------------------------
      0      | -6000       | -5000    | -5000
      1      |  2500       | -3200    | -4000
      2      |  2000       |  2500    |  3000
      3      |  1000       |  1200    |  2000
      4      |  1000       |  1200    |  1500
      5      |  1000       |  1200    |  1500
    ----------------------------------------------
    NPV @15% |   -587      |   1745    |   3665

*SENSITIVY ANALYSIS*
- Expand scenarios
- Calculate sensitivities
- Spreadsheets make this easy

*QN: Since all forecasts are essentially wrong, financial tools such as NPV and*
*IRR are weak tools in capital budgeting for financial managers*
- True
- ✓ False

*SENSITIVY ANALYSIS WRAP-UP*
- Assumptions matter
- Forecasting is an art more than a science
- There is no 100% right answer
- Understand the limitations
- Good diagnostic tool

### SPREADSHEET MODELING

*PUTTING ALL THE METRICS TOGETHER*
- Spreadsheets are a powerful tool
- Organization and best practices
- Built - in excel functions
- General layout and review of tools

[Spreadsheet Modeling Template](https://docs.google.com/spreadsheets/d/1qtE4xi3TTkn6k-__kTVkn7JbToB0YLo8Si4ZtFMt2FQ/edit?usp=sharing)
- State assumptions at top
- Note the formulas used and cells locked in formula
- Note the `IRR` and `NPV` formulas that are built in

*QN: What would happen to a project's NPV with an increase in discount rate?*
- NPV increases
- ✓ NPV decreases
- NPV stays the same

### FINANCE IN THE FIELD

Chat with Christine Boyd
- Seen wide range of budgeting tools
- smaller companies use payback more often
- Large companies rely on NPV
- NPV and IRR are the gold standard
- sales/strategy/marketing generate the NPV, not finance.
- Finace dept mostly compares multiple projects ^
- Govt regulations can cause -ve NPV you still have to do; e.g. environmental
  cleanup
- Even when losing money in project it's important to calculate NPV

### Real World Application - A Refresher on Net Present Value

[HBR - A Refresher on Net Present Value](https://hbr.org/2014/11/a-refresher-on-net-present-value)
- NPV is a method of calculating ROI

NPV
- considers the *time value of money*
- provides a concrete number that managers can use to compare an initial outlay
  of cash against ht present value of the return
- Far superior to payback method which is more commonly used
- Warren Buffet uses NPV to evaluate companies

```
             Year n Total Cash Flow
    NPV = ∑ز----------------------- ش
              (1 + Discount rate)ⁿ
```

If NPV is -ve then this is a bad project since you're draining money.

Rate of return is specific to company.
- Can be set by shareholder expectations e.g. 12% return expected
- If the company pays 4% interest on its debt then that can be used as well
- Typically the CFO's office sets the rate

3 areas where you can misestimate
- Unclear initial investment. e.g. buying equipment is fixed cost, but IT upgrade can overrun
- Discount rate is set using this year's rate but in 3 years interest rates may spike and your discount rate has to go up
- Projected returns are estimated and we tend to be optimistic in those estimates.

### MY SUMMARY

*NPV* (Net Present Value) = `IC + ∑[ CFn / (1 + r)ⁿ ]`

Excel/Google has **NPV** formula

*Payback* = `the year n at which IC = ∑CFn`

*ROIC* (Return on Invested Capital) = `(∑(Profitn)/n) / (∑(ICn)/n) * 100%`
- This includes all costs such as depreciation and reinvestment costs

*IRR* (Internal Rate of Return) = `the smallest discount rate r at which NPV = 0`

Excel/Google has **IRR** formula

IRR issues:
- It is possible to have multiple IRRs (see graph above)
- It is possible to have no IRR (see graph above)

Since the numbers used to calculate NPV is an *estimate*, we can do
*optimistic**, **expected**, and **pessimistic* cash flow projections

[Spreadsheet Modeling Template](https://docs.google.com/spreadsheets/d/1qtE4xi3TTkn6k-__kTVkn7JbToB0YLo8Si4ZtFMt2FQ/edit?usp=sharing)

### PRACTICE QUIZ

[Sheet 2](https://docs.google.com/spreadsheets/d/1qtE4xi3TTkn6k-__kTVkn7JbToB0YLo8Si4ZtFMt2FQ/edit#gid=2122363398)

1 Which project would you select based on NPVs assuming the same 7% discount
rate for both? Project A requires an initial outlay of $500 and provides an
annual income of $600 for 3 years. Project B requires an initial outlay of $400
and yields an annual income of $700 for 3 years.
- Project A
- ✓ Project B

2 Compare the two projects described directly above. Which one would you pick based on their payback periods?
- Project A
- ✓ Project B

3 What would happen to a project’s NPV with a decrease in initial investment?
- ✓ NPV increases
- NPV decreases
- NPV remains constant

4 What would happen to a project’s NPV if the estimated cash inflows are
expected sooner?
- ✓ NPV increases
- NPV decreases
- NPV remains constant

5 You are evaluating an investment that requires $5,000 upfront and pays $80 at
the end of each of the first 4 years and an additional lump-sum of $12,000 at
the end of year 4. What would happen to the IRR if the annual payments at the
end of each of the first 4 years go up from $80 to $90?
- ✓ IRR increases
- IRR decreases
- IRR remains constant

6 Assuming everything else remains the same in the prior question, what would
happen to the IRR if the initial investment decreases from $5,000 to $4,000?
- ✓ IRR increases
- IRR decreases
- IRR remains the constant

7 You are using ROI to evaluate a project that requires investments of $800 in
each of the first 4 years, and yields annual income of $200, $150, $100, and
$75 in each of the first 4 years. What would happen to ROI if the annual
incomes are halved?
- ✓ ROI halves
- ROI remains constant
- ROI doubles

8 An initial investment of $1,500 has cash flows of $900 in year 1 and $750 in
year 2. Using NPV, do you invest in this project with a discount rate of 10%?
- yes
- ✓ no

9 An initial investment of $20,000 has a cash inflow of $50,000 in year 1 and a
cash outflow of $10,000 in year 2. The firm has a cost of capital of 15%.
Calculate the IRR for this project. Should the firm accept or reject the
project?
- ✓ Accept
- Reject

10 Assume an investment costing $24,869 will earn $10,000 a year for ten years.
If the discount rate is 10%, what is the NPV of this project?
- $13,685
- ✓ $36,577
- $61,446

### WK 2 QUIZ

1 Which project would you select based on NPVs assuming the same 5% discount
rate for both? Project A requires an initial outlay of $1,000 and provides an
annual income of $500 for 3 years. Project B requires an initial outlay of
$2,000 and yields an annual income of $900 for 3 years.
- Project A
- ✓ Project B

2 Compare the two projects described directly above. Which one would you pick
based on their payback periods?
- ✓ Project A
- Project B

3 What would happen to a project’s NPV with an increase in initial investment?
- NPV increases
- ✓ NPV decreases
- NPV remains constant

4 What would happen to a project’s NPV if its cash inflows are pushed further
into the future?
- NPV increases
- ✓ NPV decreases
- NPV remains constant

5 You are evaluating an investment that requires $1,000 upfront, and pays $50
at the end of each of the first 2 years, and an additional lump-sum of $1,000
at the end of year 2. What would happen to the IRR if the annual payments at
the end of each of the first 2 years go down from $50 to $40?
- RR increases
- ✓ IIRR decreases
- IRR remains constant

6 Assuming everything else remains the same in the prior question, what would
happen to the IRR if the initial investment increases from $1,000 to $1,050?
- IRR increases
- ✓ IRR decreases
- IRR remains constant

7 You are using ROI to evaluate a project that requires investments of $500 in each of the first 3 years, and yields annual income of $100, $75, and $50 in each of the first 3 years. What would happen to ROI if the annual incomes double?
- ROI halves
- ROI remains constant
- ✓ ROI doubles

* 7/7 correct

## WEEK 3: MEASURING CASH CREATION AND FLOW

### INTRO

CASH IS KING!
- Review the financial statements
- Measure cash creation
- **FCF** Free cash flow measures
- Taxes
- Terminal/salvage values
- DCF valuation

### BRIEF OVERVIEW OF THE FINANCIAL STATEMENTS

*THE MAIN FINANCIAL STATEMENTS*
- Balance Sheet: Assets owned
- Income Statement (P&L): Net sales
- Cash Flow Statement: Reconciles top 2

*BALANCE SHEET*
- What does the firm own?
- How was it paid for?
- `Assets = Liabilities + Owner's Equity`

*ASSETS ON THE BALANCE SHEET*
- Current Assets
  - Cash and marketable securities
  - Accounts receivable
  - Inventories
- Property, Plant, and Equipment
  - Land, buildings
  - Machinery
  - Accumulated depreciation
- Other Assets (e.g. Intangibles) e.g. Brand of Coca Cola

*THE OTHER SIDE OF THE BALANCE SHEET*
- Liabilities
  - Short term (payables, current debt, etc.)
  - Long term (deferred taxes, long - term debt)
- Shareholders equity
  - Preferred and common stock (par value)
  - Retained earnings

*INCOME STATEMENT* Net Sales (Revenue)

    Net Sales (Revenue) =
      - Cost of goods sold
      - SG&A expense
        = EBITDA

      - Depreciation and Amortization
        = EBIT (“pre-tax operating profit”)

      - Interest expense
        = Taxable income

      - Income tax
      - Dividends (if any) =
    ----------------------------------
    Net Income (Profit or “earnings”)

*STATEMENT OF CASH FLOWS*

- Accrual method of accounting: generally book sales before we receive money
- Reports on cash movements across activities:
  - Operating (net income, depreciation)
  - Investing (capital expenditures, sale of assets)
  - Financing (dividends, new debt)
- Reconciles balance sheet/income statement

QN: As a metric for free cash flows of the firm, EBITDA is the revenue less the
cost of goods sold, sales general and administrative costs, depreceiation,
interest and taxes
- true
- ✓ False

EBITDA is a metric for the free cash flows generated by the operations of the
firm, independent of tax rate and the levels of debt within the firm.
Therefore, EBITDA is pulled from the accounting statement prior to
depreciation, interest and tax expense

*SUMMARY: ACCOUNTING STATEMENTS*

- Report the financial condition
  - Balance Sheet
  - Income Statement
  - Statement of Cash Flows
- Apples to apples
- GAAP rules
- Treasure map for real cash!

### HUNTING FOR CASH CREATION

Purpose of accounting statements are due to financial statements. But may not
give full picture of where cash is hidden

*HUNTING FOR CASH*

- Earnings != cash
- Accruals != cash
- Book value != market value ; book value may have been 20 yrs ago and doesn't
  account for current value
- Accounting cost != economic cost ; even though a machine may be depreciated
  doesn't mean it's not working

*ACCOUNTING EARNINGS*
- You cannot spend earnings
- Noncash expenses
- Extraordinary items
- Balance sheet changes
- We must find cash flow!

QN: Accounting earnings or bottom-line net income is an accurate representation
of the cash creation of the firm
- true
- ✓ False

Accounting must incorporate write-downs for such tings as depreciating assets
that are not reflective of cash creation for the firm in that period

*CASH IS KING!*
- Only cash matters in the end
- Not all cash is paid out
- Need a measure of cash creation
- Consistent over time and across firms
- Free Cash Flow **FCF**: how much money can i scrape up if i _had to_ in order
  to pay investors

*FREE CASH FLOW (FCF)*

We'll talk about:
- Working capital
- Depreciation (non-cash)
- Capital expenditures
- Asset sales (salvage, terminal)
- Taxes

     FCF = Operating Profit (after tax)
         – Increase in WC (Working Capital)
         + Depreciation
         – Capital expenditure
         + After tax salvage value

*SUMMARY*

- NPV, IRR, etc. based on cash
- Cash creation (not earnings) will drive valuation
- Measuring FCF is paramount

### WORKING CAPITAL ADJUSTMENTS

*WORKING CAPITAL* and how it impacts measure of cash flow

- `WC = Current Assets – Current Liabilities`
- Operating liquidity
- measures Opportunity cost
  - WC cannot be deployed elsewhere
- Not included as an expense!

*CURRENT LIABILITIES*

Examples:
- Liabilities to be settled < 1  year
- Accounts payable
- Current portion of debt due < 1 yr
- Increase in CL is a cash source ; expect cash to come in
- Decrease in CL is a cash drain

*CURRENT ASSETS*

Examples:
- Sold, consumed, or exhausted in 1 year
- Accounts receivable
- Inventory
- Increase in CA is a cash drain
- Decrease in CA is a cash source

QN: How does an increase in Current Liabilities affect cash?
- ✓ Increases Cash
- Decreases Cash
- No effect on Cash

An increase in Current Liabilities represents an increase in cash which the
firm owes within 1 year

*working capital: example*

             Quarter | 0   | 1   | 2   | 3
    ----------------------------------------

    Assets
    ----------------------------------------
            current  | 100 | 125 | 135 | 100
            longterm | 150 | 150 | 150 | 150
    ----------------------------------------
    Total Assets     | 250 | 275 | 285 | 250
    ----------------------------------------

    Liabilities
    ----------------------------------------
            current  |  75 |  65 |  65 | 100
            longterm |  80 |  80 |  80 |  80
    ----------------------------------------
    Total Liabi.     | 155 | 145 | 145 | 180
    ----------------------------------------

    ----------------------------------------
    Net Worth        |  95 | 130 | 140 |  70
    ----------------------------------------

    ------------------------------------------------------------------
        Working Cap. |  25 |  60 |  70 |   0 | = Curr Ass - Curr Liab
        Change in WC |  25 |  35 |  10 | -70 | = WC(n+1) - WC(n)
    ------------------------------------------------------------------

QN: What is net working capital?
- Shareholders equity less assets
- ✓ Current assets minus current liabilities
- Debt less assets

Working capital represents money that is owed to or owed from the firm within
the next year that has not yet come in or out as cash, including such things as
money invested in inventory which has not yet been sold and money which has not
yet been received from customers for goods received

*FCF - FREE CASH FLOW*

     FCF = Operating Profit (after tax)
         – Increase in WC
         + Depreciation
         – Capital expenditure
         + After tax salvage value

*increase in WC => cash is flowing out from the firm*

*SUMMARY*

- Working capital is an opp. cost
- Increases in WC are a cash drain
- WC Not reflected in earnings
- FCF needs to account for WC changes

### DEPRECIATION AND CAPITAL EXPENDITURES

*DEPRECIATION AND AMORTIZATION*

Examples:
- Wear and Tear on assets
- ^ leads to Loss of value
- recorded as a Non-cash expense; Not actual money that left the firm
- Amortization for intangibles; e.g. reduction in brand value
- *These are Included in earnings*

*CAPITAL EXPENDITURES* **CAPEX**

- Buying/replacing long - term assets
- Property, plant, equipment
- This spending not reported in earnings; not used to generate sales
- *Need to be subtracted for FCF*

Want to spread out CAPEX over budget period. Reflects ongoing cost of doing business.

QN: To get to FCF from accouning earnings
- ✓ Add back depreciation and ammortization and subtract capital expenditures
- Subtract depreciation and ammortization and add back capital expenditures

D&A is not a cash expense so it is added back to get to FCF. Cap Ex is a cash
expense not included in accounting earnings so it is subracted to get to FCF.

*FCF - FREE CASH FLOW*

     FCF = Operating Profit (after tax)
         – Increase in WC
         + D&A
         – CAPX
         + After tax salvage value

*SUMMARY*

- D&A is noncash reflected in earnings
- Add D&A back for FCF
- CAPX is cash not reflected in earnings
- FCF needs to account for CAPX

### SALVAGE AND TERMINAL

*SALVAGE AND TERMINAL VALUES* What happens when we sell assets on the balance
sheet

- CAPX is spending cash
- Selling assets generates cash; Not reflected in P&L
- Asset sales go into FCF

*THE END OF THE PROJECT*

- The balance sheet is real; represents a real physical asset
- PP&E (property plant & equipment) cannot vanish
- Balance sheet must “sweep clean”
- We have to sell off anything on the books at the end of a project

*TERMINAL/SALVAGE VALUES*

    Projected Balance Sheet   |  0  |  1  | 2
    --------------------------------------------
    Cash and Marketable Sec.  |  75 |  75 | 200
    Other Current Assets      |   0 | 100 |  75
    --------------------------------------------
    Fixed Assets
    ---------------------------------------------------------------------------------
      At cost                 | 500 | 500 | 500 | spent this amount to buy an asset
      Accumulated Deprec      |   0 | 100 | 200 | deprec on asset
      Net Fixed Assets        | 500 | 400 | 300 | At cost - Accum. deprec
    --------------------------------------------
    Total Assets              | 575 | 575 | 575
    --------------------------------------------

    --------------------------------------------
    Current liabilities       |  75 |  75 |  75
    LT Debt                   | 250 | 250 | 250
    Total liabilities         | 325 | 325 | 325
    --------------------------------------------
    Stock and acc ret earning | 250 | 250 | 250
    --------------------------------------------
    Total liab. & equity      | 575 | 575 | 575

*Net Fixed Assets* is the amount I have to account for as salvage.
- Have to do something with it e.g. sell it or move it to another project

QN: A piece of eq costs $1500. If this asset depretiates on a 5 yr schedule,
the Net Fixed Asset value on the Balance Sheet in year 1 will be more or less
than this same asset depreciating on a 3 yr schedule?
- ✓ More
- Less
- No Impact

Net Fixed Asset depreciation = Cost - ( Cost / years )

*WHAT IF WE DON’T SELL THE ASSETS?*

- Doesn't matter. Assets are an opportunity cost
- Moving assets has a cost
- Each project is separate
- Transfer pricing; Have to account for moving the asset
- Best practice always sweeps clean the balance sheet; Even if I'm not selling
  asset I have to pretend I am

QN: The firm sells a piece of equipment no longer needed for oepration. This
asset has a book value of $1000. What impact does this sale have on FCF?
- ✓  Increases FCF
- Decreases FCF
- No impact on FCF

*The salvage of an asset increases FCF*

*TERMINAL/SALVAGE VALUES*

     FCF = Operating Profit (after tax)
           – Increase in WC
           + Depreciation
           – Capital expenditure
           + After tax salvage value

*SUMMARY*

- Assets sales must be included in FCF
- Balance sheet must always sweep clean; have to sell everything at end of
  project
- Each project must stand alone; cannot share assets across projects
- Opportunity costs are key; have to reflect up front cost to purchase and
  salvage at end

### TAXES

*FREE CASH FLOW AND TAXES*

- Taxes are a real cash flow
- Expenses shield revenue from tax; ie expenses reduce taxes owed e.g. business
  expenses
- Tax forecasting is tricky

*FREE CASH FLOW AND TAXES*

- Assume taxes paid at marginal rate; not accounting for tax loophole shenanigans
- Can make use of all shields
- Ignore tax loss and carryforward
- A whole world of tax accounting!
- Our treatment is simplified

That is to say for this course we're assuming taxes are simple. In the real
world they get complicated fast

QN: Interest expense provides a tax shield for the firm.
- True
- False

Interest expense is deducted from earnings before the tax rate is applied

*SUMMARY*

- Taxes are real cash
- Can be difficult to forecast; require tax professionals to deal with
- Often drive financial decisions
- Full scope beyond this course

### CALCULATING FREE CASH FLOW

*FREE CASH FLOW*

     FCF = Operating Profit (after tax)
           – Increase in WC
           + Depreciation
           – Capital expenditure
           + After tax salvage value

*LET’S WALK THROUGH A SIMPLE EXAMPLE*

| Year                    | 0     | 1   | 2   | 3   |                                           |
| ----------------------- | ----: | --: | --: | --: | :-----------------------                  |
| Revenue                 |       | 500 | 500 | 500 |                                           |
| Total Costs             |       | 300 | 300 | 300 |                                           |
| * Depreciation          |       | 100 | 100 | 100 |                                           |
| ----------------------- | ----- | --- | --- | --- | ------------------------                  |
| EBIT                    |       | 100 | 100 | 100 | = Rev - Costs - Depr                      |
| Taxes (30%)             |       | 30  | 30  | 30  |                                           |
| ----------------------- | ----- | --- | --- | --- | ------------------------                  |
| * NOPAT                 |       | 70  | 70  | 70  | Net Oper Profit after Tax                 |
|                         |       |     |     |     |                                           |
| * Cap Spending          | 500   | 0   | 0   | 0   | Up front expense                          |
| Net PP&E                | 500   | 400 | 300 | 200 | Value - Depreciation                      |
| Cash from Ops           | 0     | 170 | 170 | 170 |                                           |
| * Working Capital       | 150   | 100 | 50  | 0   | CAPX = WC(n-1) - WC(n)                    |
| * Terminal (Ass Sales)  | 0     | 0   | 0   | 200 |                                           |
| ----------------------- | ----- | --- | --- | --- | ------------------------                  |
| Free Cash Flow          | -650  | 220 | 220 | 420 | NOPAT - Diff(WC) + Depr - CAPX + Ass Sale |

`FCF = NOPAT`

QN: A company has an operating income of 100, depreciation of 5, asset sale of
50, and a capital expenditure of 10. Calculate this company's FCF for the year

- 145

| Income        | 100 |                              |
| Depreciation  | 5   |                              |
| Asset sale    | 50  |                              |
| CAPX          | 10  |                              |
| ------------- | --- | ---------------------------- |
| FCF           | 145 | = Income + Dep + Sale - CAPX |


### USING CAPITAL BUDGETING TOOLS

*FREE CASH FLOW*

     FCF   = Operating Profit (after tax)
           – Increase in WC
           + Depreciation
           – Capital expenditure
           + After tax salvage value
       
     => NPV
     => IRR
     => Payback
     => ROIC

### Homework Assignment

[worksheet](https://docs.google.com/spreadsheets/d/12rvN8MPYjxo_vQ9h5C10CQPv9vxmOvuPQZq0a_vwQyo/edit#gid=0)

1 Machine A costs $5,000 and depreciates on a 4-year schedule. Machine B costs $4,000 and depreciates on a 5-year schedule. Which machine has a higher Net Fixed Asset value on the Balance Sheet in year 1?
- ✓ Machine A
- Machine B
- They are the same

2 A company has an operating income of $200 million, no depreciation, an asset sale of $75 million, a capital expenditure of $30 million, and no changes in net working capital. Calculate this company’s free cash flow for the year.
- $95 million
- ✓ $245 million
- $305 million

3 A project requires an initial investment of $2.8 million. This initial investment is to be depreciated straight-line to 0 in 4 years. What is the annual depreciation amount?
- $466,666.67
- $333,333.33
- $500,000
- ✓ $700,000

4 Suppose the investment described above generates an annual sales of $2,360,000, with annual costs of $520,000. Assume a tax rate of 35%. What is the tax to be paid on annual sales?
- $182,000
- ✓ $644,000
- $826,000

5 What would be the tax savings from depreciation?
- $178,666.67
- $200,000
- ✓ $245,000

6 What is the annual operating cash flow from this project?
- $951,000
- ✓ $1,441,000
- $2,729,000

7 Suppose Company XYZ has revenues of $700 million, cost of goods sold of $200 million, and depreciation of $50 million. What is the company’s EBIT?
- $400 million
- ✓ $450 million
- $550 million
- $950 million

8 Suppose XYZ also pays a 25% tax. What would be the company’s NOPAT?
- $100 million
- ✓ $337.5 million
- $450 million

9 Company XYZ has, in addition, an increase in net working capital of $80 million, and capital expenditure of $30 million. What is XYZ’s FCF?
- $177.5 million
- 237.5 million
- ✓ $277.5 million
- $437.5 million

10 A project requires an initial investment of $750,000 depreciated straight-line to $0 in 4 years. The investment is expected to generate annual sales of $400,000 with annual costs of $120,000 for 4 years. Assume a tax rate of 30% and a discount rate of 14%. What is the NPV of the project?
- ✓ -$15,016
- $367,409
- $734,984
- -$561,337

^ Calculate FCF and use that to calculate npv = (Investment) - npv(discount rate, FCF1:FCF4)

### Quiz

[Worksheet 2 "Quiz"](https://docs.google.com/spreadsheets/d/12rvN8MPYjxo_vQ9h5C10CQPv9vxmOvuPQZq0a_vwQyo/edit#gid=1938408631)

1 An increase in net working capital means
- An increase in cash
- ✓ A decrease in cash
- No change in cash

**I don't get this**

2 A company has an operating income of $100 million, no depreciation, an asset sale of $50 million, a capital expenditure of $10 million, and no changes in net working capital. Calculate this company’s free cash flow for the year.
- $145 million
- ✓ 140 million
- $135 million
- $155 million

`FCF = Op. Income + Asset Sale - CAPX = 100+50-10=140`

3 A project requires an initial investment of $1.4 million. This initial investment is to be depreciated straight-line to 0 in 3 years. What is the annual depreciation amount?
- ✓ $466,666.67
- $333,333.33
- $500,000
- $666,666.67

`Depreciation = Investment/years = $1.4M / 3 = $ 0.467M`

4 Suppose the investment described above generates an annual sales of $1,120,000, with annual costs of $480,000. Assume a tax rate of 35%. What is the tax to be paid on annual sales?
- $274,000
- $250,000
- ✓ $224,000

`Annual tax paid = (Annual Sales - Annual Cost) * Tax Rate = (1120000-480000)*0.35 = 224,000`

5 What would be the tax savings from depreciation?
- $200,000
- ✓ $163,333.33
- $178,666.67

`Tax Savings = Tax rate * Depreciation = 0.35*466666.67 = 163,333.33`

6 What is the annual operating cash flow from this project?
- $780,000
- $466,666.67
- ✓ $579,333.33


`Operating Cash Flow = Sales - Costs - Tax + Deprec. Tax Saving = 1120000 - 480000 - 224,000 + 163,333.33 = 579,333.33`

7 Suppose company XYZ has revenues of $500 million, cost of goods sold of $300 million, and depreciation of $100 million. What is the company’s EBIT?
- ✓ $100 million
- $200 million
- $300 million
- $400 million

`EBIT = Sales - Costs - Depreciation = $500-300-100 = 100`

8 Suppose XYZ also pays a 30% tax. What would be the company’s NOPAT?
- ✓ $70 million
- $100 million
- $130 million

`NOPAT = EBIT * (1 - Tax rate) = 100*(1-30%) = 70`

9 Company XYZ has, in addition, an increase in net working capital of $50 million, and capital expenditure of $10 million. What is XYZ’s FCF?
- ✓ $110 million
- $100 million
- $90 million

`70 (NOPAT) + 100 (Dep) – 50 (NWC) -10 (CAPEX) = 110`

## WEEK 4: RISK, RETURN, AND THE COST OF CAPITAL

### INTRO

How to calculate **rate or return r**

- Debt vs. Equity: differnet sources of income
- Cost of equity
- Cost of debt
- Weighted average cost of capital
- Putting it all together

### DEBT VS. EQUITY FINANCING

*DEBT VS EQUITY*

    Simple Balance Sheet
           |
    --------------------
           |
     Stuff | Debt
           |
           | Equity

2 Sources of Capital
- **Debt** `Rd`
- **Equity** `Re`

`WAC = Rd + Re`

*DEBT FINANCING*
- Non-contingent claim: has to be paid back whether or not company is profitable
- Repay principle and interest
- Collateral
- Priority in bankruptcy: Sr debt holders get paid back first
- Monitoring / restrictions: have a lot of rules and regulations
- Many different forms

*SOURCES OF DEBT*
- Banks
  - Straight loan
  - Line of credit
  - Mortgages
  - Commercial/industrial loans
- Bonds

*DEBT FINANCING AND TAXES*
- Interest payments are pre-tax
  - Creates a tax shield
  - This is an important cash flow
  - Subsidizes debt
  - Lowers the effective interest rate

*EQUITY FINANCING*
- Ownership and control: issuing shares in the company
- Contingent claim
- Equity holders get all residual cash
- Equity holders get all the upside
- Wiped out in bankruptcy: Equity holders also hold the risk

QN: Increasing the debt of the firm decreases the cash taxes owed
- ✓ True
- False

Debt creates a *tax shield* because interest expense is *subtracted from
pre-tax earnings*, lowering the actual cash taxes owed

*MIX OF DEBT AND EQUITY*
- **Capital structure**: the mix of debt and equity
- Does not change risk! Debt shifts the risk to the equity holders
- Moves risk between investors
  - Debt: no upside / protected downside
  - Equity: all upside / can get wiped out

*SUMMARY*
- Equity has ownership and control
- Debt is safer than equity
  - Lower cost
- Mix is called “capital structure”
  - Slices up the risk of the firm

### RISK-FREE RATE

Safest possible investment?
- put money under mattress: house could burn down or deflation
- gold: volatile
- put in bank: insured by FDIC which is backed by US Treasury Bonds
  - cut out middle man (bank) and go straight to Bonds

*US TREASURY BONDS*
- US will not default (at least anytime soon)
- Treasury can print money
- Backed by future taxes
- Treasury rate is safest

*RISK FREE RATE*

Whether you buy GE bonds or Facebook Stock implies I want a return

    Rate of return = risk free rate
                   + risk premium

*HISTORICAL RATES*

Between 5-7% with a large spike in 1980s
- true for even older ecomonies we have data for e.g. ancient rome, medieval england, England in 1800s
- 5-7 seems to be the sweet spot

![Long Term Treasurey Rate](https://drive.google.com/uc?id=0BwjXv3TJiWYEd0hCZUNpaHA5ZzA)

*RISK FREE RATES: MATURITY*

- Yield curve
- Longer maturity = higher rates
  - Rates may rise
  - Greater liquidity risk:
- longer the maturity the greater the risk ie want a better rate

*SUMMARY*

- Risk free rates set the floor
- Risky returns earn a premium
- **Benchmark is U.S. Treasury**
- Rates rise with maturity

### HISTORICAL RISK AND RETURN

*HISTORICAL RATES OF RETURN*

![Historical return rates](https://drive.google.com/uc?id=0BwjXv3TJiWYEVHo0ci00RlJrbUk)
- Stock market historically provided greatest risk premium
- Greater risk => greater returns
- These numbers occured organically

Tabular data of above graph:

|                 | Inflation | T.Bills | T.Bonds | C.Bonds | Stocks |
| --------------- | --------: | ------: | ------: | ------: | -----: |
| Mean return     |   3.0%    |    3.5% |    5.2% |    7.2% |  11.4% |
| Standard Dev    |   4.2%    |    3.1% |    7.8% |    7.8% |  19.8% |
| Minimum         | -10.1%    |    0.0% |  -11.1% |   -8.9% | -43.8% |
| 25th percentile |   1.2%    |    1.0% |    1.2% |    2.9% |  -1.2% |
| Median          |   2.7%    |    3.1% |    3.5% |    5.2% |  13.9% |
| 75th percentile |   4.2%    |    5.2% |    8.5% |   10.8% |  25.3% |
| Maximum         |  18.1%    |   14.3% |   32.8% |   35.5% |  52.6% |

- standard deviation == volatility
- even though stocks have best return, they're most volatile
- stock max = 52.6 and min = -43.8. i.e. lots of risk

**higher risk ==> higher expected returns (discount rate)**

*IN THE LONG RUN*

- stocks better in the long run
- Might need 50 years
- Huge volatility
- Higher discount rates

*RISK AND RETURN*

- `Rate of return = risk free rate + risk premium`
- More risk drives higher returns due to:
  - time value of money
  - opportunity costs

*SUMMARY*
- stocks return around 12%
- Interest rates are around 6%
- Stock volatitility much higher
- long rates > short rates

### THE EQUITY RISK PREMIUM

*EQUITY RISK PREMIUM*

- Stocks do better in the long run
- Might need 50 years!
- Huge volatility: long periods e.g. 20 years, before I see returns
  - If we lived longer this would be better but if close to retirement it's too risky
- Higher discount rates!

*STOCK MARKET PERFORMANCE*
- The stock market returns 10-12%
- Interest rates are typically 5-6%
- **Equity premium = Rm (return on market) – r.f. (risk free rate)**  = `11% – 5.5%` = `5.5%`
  - ^ What is the price of stock market risk?

*EQUITY RISK PREMIUM*

- 5.5% is based on historical average
- Does this seem reasonable?
- Surveys of market professionals differ
- Different methods give 4% - 8%!

*EQUITY PREMIUM*

- 4.5% – 6.5% is a good range
- Why might this change over time?
  - Systemic risk
  - Attitudes toward risk
- These change the price of risk!

*SUMMARY*

- Stock market as a whole is well diversified - not just one stock
- Equity premium is around 4.5-6.5%
- Compensates for equity risk
- 5.5% ballpark “price” of market risk

### BETA AND THE COST OF EQUITY

*EQUITY RISK ON STOCKS*

- Equity market premium is 5.5%
- Premium for a single stock?
- How to measure stock risk?

*MEASURING STOCK RISK*

- What makes a single stock risky?
  - Wiggles a lot?
  - “Jumps” around too much?
  - Has gone down in the past?
- These are all stock specific risks....
- **Diversification reduces these risks!**

*HOLD MULTIPLE STOCKS!*

Historical return on 3 stocks:

![Hold Multiple Stocks!](https://drive.google.com/uc?id=0BwjXv3TJiWYEOW9oMEpPeHBMZTA)
- The 3 stocks have mixed volatility

But if we have diversified across the 3 stocks above our return is 14% (+/-12%)

![Diversified portfolio](https://drive.google.com/uc?id=0BwjXv3TJiWYEQ1k1dXpNOVBEXzg)

QN: Over the years 2051 to 2060 the average annual return on the overall stock
market is 10% and the average risk-free rate is 3%. Waht is the stock market
risk permium during those 10 years?
- 7%

    Equity premium = Rm - Rf
                   = 10 - 3 = 7%

*DIVERSIFICATION*

- Holding multiple stocks reduces risk!
- Why not hold lots of stocks?
- Why not hold the market?

*HOW TO MEASURE RISK*

- Wiggles and jumps might be good if the wiggle is independant of the rest of the market
- How does a stock change my portfolio?
- Does a stock make me wiggle more or less?

*BETA: ONE MEASURE OF RISK*

- How much wiggle with the market?
- Variance (wiggle)
- Covariance (wiggle together)

QN: What is a measure of an asset's riskiness?
- Risk free rate
- ✓ Beta
- Market risk premium

**Beta** measures how much a stock moves relative to the overall market and
represents the riskiness of the asset

    Ri = Rate of stock
    Rm = Rate of market

    Beta = Β = Cov(Ri, Rm) / Var(Rm)

*MARKET BETA*

- Average beta around 1
- Most betas between 0.25 and 2.5
- Beta = 2  :  Stock return up/down (wiggle) twice the market return
  - Two servings of market risk
  - Should have higher returns

*COST OF EQUITY*

    Rate of return = risk free rate
                   + risk premium

    Risk Premium   = Beta * (Equity Premium)

*CAPITAL ASSET PRICING MODEL (CAPM)*

    Return = risk free rate
           + Beta * (Equity Premium)

*COST OF EQUITY USING CAPM*

Stock has a beta of 1.8.

Equity premium is 5.5%.

Risk-free rate is 3%.

What is the cost of equity?

    Re = r.f. + Beta * (equity premium)
       = 3% + 1.8 *(5.5%)
       = 12.9%

i.e. I should expect a return of 12.9% on a stock with a beta of 1.8%

QN: Stock A has a beta of 0.8, whereas stock B has a beta of 1.5. Which one do
you expect to provide a higher return?
- Stock A
- ✓ Stock B

*COST OF EQUITY (Re)*

    Simple Balance Sheet

          |
    --------------------
          |
    Stuff | Debt
          |
          | Equity (Re)
          |

*SUMMARY*

- Diversification changes risk
- Market risk can’t be diversified
- Beta is sensitivity to market risk
- `Re = r.f. + Beta * (Equity Premium)`

### CREDIT RATING AND QUALITY

*WHAT MAKES DEBT RISKY?*

    Rate of return = risk free rate
                   + risk premium
                      ^    ^
    Default ----------|    |
                           |
    Recovery in default ---|

- Default == company not paying back default

*MEASURING RISK FOR DEBT*

- Will the debt default?
  - Maturity
  - Cash on hand/ Capital cushion
  - Debt level
  - Profitability
  - Economic conditions
  - Ability to raise capital

*MEASURING RISK FOR DEBT*

- Can I recover my money in default?
  - Physical capital / Tangibility
  - Marketability
  - Transportability

QN: The availability of physical assets within a firm is a factor in evaluating
the riskiness of the firm's debt
- true

*CREDIT RATING AGENCIES*

- Banks and credit rating agencies track the credit worthiness rating
- Estimate default/recovery
- Assign a classification (credit score)
- This gives a risk premium

*AVERAGE YIELDS ON DEBT (Rd)*

Example from October 2015 Average US Corporate Bond Yields

|Rating      | 1yr  | 5yr  | 10yr | 20yr |
| ---------- | ---- | ---- | ---- | ---- |
|US Treasury | 0.2% | 1.4% | 2.0% | 2.5% |
|AAA         | 0.4% | 1.9% | 2.8% | 3.7% |
|AA          | 0.5% | 2.0% | 3.3% | 4.0% |
|A           | 0.7% | 2.2% | 3.5% | 4.2% |
|BBB         | 1.2% | 2.9% | 4.6% | 5.2% |
|BB          | 2.0% | 4.8% | 5.7% | 6.1% |

- longer term has higher return
- as credit quality goes down, returns go up

*SUMMARY*

- Risky debt earns a premium
- Default and recovery are the source of risk
- Credit scores and rating help determine how risky debt is

### ESTIMATING THE COST OF DEBT

*INTRO*

      Rate of return = risk free rate
                     + risk premium

3 methods to put a risk premium:
- Historical cost
- Current yield to maturity
- Ratings adjusted yield

*COST OF DEBT CAPITAL*

- Historical cost
  - What did the company pay last time?
  - Look at interest expense over debt
  - What is the coupon rate on bonds?
- ^ OK method, but not great
  - May not reflect current market
  - Rates may have changed

*COST OF DEBT CAPITAL*

- Current yield to maturity is probably best method
- ^ Best method only works:
  - If you have market prices
  - Mainly large public companies

*COST OF DEBT CAPITAL*

- Ratings adjusted yield
  - Debt rating/credit score
  - Current treasury rate. Bond return is dependable
- Adjust the treasury rate by the “credit spread”

QN: Suppose the risk-free rate is 5%. In average an AAA-rated corporate bond carries a credit spread of 0.1%, An A-rated corp bond carries a credit spread of 1%, and a B-rated corp bond carries a credit spread of 3%. Company XYZ's outstanding debt is rated A by rating agencies. What would be the cost of debt for XYZ based on prevailing market rates?
- 6% `r.f. + Risk = 5% + 1%`

*EXAMPLE OF RATINGS ADJUSTED YIELD:*

What is Rd for a 10-year A-rated firm? Based on table below `Rd = 2.0% + 147 b.p. = 3.47%`

Basis point spreads based on market prices
| Rating      | 1yr  | 5yr  | 10yr | 20yr |
| ----------- | ---- | ---- | ---- | ---- |
| US Treasury | 0.2% | 1.4% | 2.0% | 2.5% |
| AAA         |  21  |  53  |   76 |  122 |
| AA          |  30  |  65  |  121 |  153 |
| A           |  43  |  88  |  147 |  175 |
| BBB         |  96  | 153  |  253 |  269 |
| BB          | 172  | 343  |  361 |  364 |


*IMPORTANCE OF TAXES*

- Interest payments are deductible
- The effective cost of debt is less than what you pay

    tc = tax rate

    Rd = R (1 - tc)

Example: You pay `5%` on debt and have a `20%` tax rate.
- `$5` goes to the bank
- Your taxes go down by `20% * $5 = $1`
- So you only really paid `$4`
- Effective cost of debt is `4%`

*SUMMARY*

- `Rd` reflects default and recovery
- Historical cost of debt
- Current yield on debt
- Ratings adjusted yield
- Interest is tax deductible


### PUTTING IT ALL TOGETHER AS THE WACC

*COST OF CAPITAL*

    Simple Balance Sheet
            |
    -------------------
            |
     Stuff  | Debt (Rd)
            |
     (WACC) | Equity (Re)
            |

               Equity               Debt
    WACC = ------------- * Re + ------------- * (1-tc) * Rd
           Equity + Debt        Equity + Debt

    Rd = Rate of debt
    Re = Rate of equity
    t = tax rate

- Cost of capital for the firm
- Balances debt and equity

QN: Company XYZ has a target capital structure of 50% equity and 50% debt. Its cost of equity is 10% and cost of debt is 5%. What is XYZ's weighted average cost of capital (WACC)? Suppose there is no tax?

    WACC = (50 / 100) * 5% + (50 / 100) * 10%
         = 2.5 + 5
         = 7.5%

*WACC: AN EXAMPLE*

Example:
- The equity value of Target is about `$40B`. (equity)
- They have roughly `15B` in long-term debt.  (debt)
- They pay a `35%` corporate tax rate.
- Their beta is `0.6`.
- Assume treasury rates are `2.5%` and the equity premium is `5.5%`.
- They are A-rated with a quality spread of `120bps`.

Estimate Target’s cost of capital

    E           = 40
    D           = 15
    r.f.        = 2.5%
    B           = 0.6
    eq prem     = 5.5%
    qual spread = 120bps
    tc          = 35%

    E / (D + E) = 40 / 55 = 72.7%
    D / (D + E) = 27.3 %

    Re = r.f. + B * eq prem
       = 2.5% + 0.6 * 5.5%
       = 5.8% (What shareholders should expect to earn)

    Rd = r.f. + qual sp
       = 2.5% + 1.2%
       = 3.7% (what debt holders should expect to earn)

    WACC = (72.7 * 5.8) + (27.3 * 65 * 3.7)
         = 4.87%

**WACC == the discount rate I would use in calculation previous e.g. npv, payback rate, etc**

QN: Company XYZ has a target capital structure of 50% equity and 50% debt. Its
cost of equity is 10% and cost of debt is 5%. What would happen to XYZ's WACC
if its capital structure were to shit to 75% equity and 25% debt?
- WACC increases

A shift to put more weight on equity raises WACC in this example because cost
of equity is higher than cost of debt


*WACC: SUMMARY*

- Firm’s cost of capital ==> WACC
- Weighted average of debt and equity
- Debt receives tax shield

### CONVERSATIONS WITH A PRACTITIONER

Cost of Capital is very important
- can be tricky to calculate
- firms will sometimes use a ballpark estimate e.g. 10%

Mature companies makes sense to use a conservative estimate

Increased debt doesn't make the company riskier, just pushes the risk to
another place

Taking on debt makes the equity riskier, not the overall company riskier.
- but it also adds a tax shield

[U.S. Oil companies closer to balancing capital investment with operating cash flow](https://www.eia.gov/todayinenergy/detail.php?id=27112)
- As oil companies' spending falls and crude oil prices increase, the need for
  oil companies to find external sources of funding may decline, which could
  reduce financial strain in the coming quarters.
- The difference between operating cash flow and capital expenditure — known as
  **free cash flow** — represents whether a company can pay for its investment
  through its after-tax profits.

[Why aren't companies spending?](http://www.economist.com/blogs/buttonwood/2015/08/business-investment)

### PRACTICE QUIZ

1 What happens to a firm’s WACC if the firm’s tax rate increases?
- WACC increases
- ✓ WACC decreases
- WACC remains constant

    An increase in tax rate effectively decreases the cost of debt, decreasing WACC

2 Company XYZ has a beta of 1.4. Assume the Treasury bond rate is 6%, and the
risk premium is 8.5%. What is the expected return on XYZ’s stock?
- 21.3%
- 13.65%
- ✓ 17.9%
- 8.5%

    Re = r.f. + B * eq prem
       = 6 + 1.4 * 8.5

3 A stock has an expected return of 15.3%, the risk-free rate is 5%, and the
market risk premium is 8%. What must be the beta of this stock?
- 0.75
- 0.85
- ✓ 1.29
- 1.46

    B = Re - r.f. / eq prem
      = 15.3 - 5% / 8

4 Company XYZ has a target capital structure of 60% equity and 40% debt. Its
cost of equity is 12%, and cost of debt is 6%. Suppose there is no tax. Should
the company take on a project that demands an initial investment of $600
million, and provides an income of $800 million in 2 years?
- ✓ yes
- no

    WACC = ((E / D+E) * Re) + ((E / D+E) * Rd)
          = 60/100 * 12 + 40/100 * 6
          =  7.2 + 2.4
          = 9.6%

    FV = PV * (1 + r)^t
       = 600 * (1 + 9.6%)^2
       = $720.73 million

    Since 800m is greater than 720m  this is a good investment

5 In the above example, if the income of $800 million comes in 4 years instead of 2 years, should the company take the project?
- yes
- ✓ no

    FV = 600 * (1 + 9.6%)^4 = 865m

6 A company has 35% of its assets financed by debt. What is this company’s
debt-equity ratio?
- 75%
- 66.6%
- ✓ 53.8%
- 33.3%

    ratio = D / E * 100%
    35 / 65 * 100 = 53.8

7 A company has a debt-equity ratio of 40%. How much of this company’s assets
are financed by equity?
- 40%
- 60%
- 66.6%
- ✓ 71.4%

    D/E = 40% => D = 40, E = 100

    E / D+E = 100/140 = 71.4

8 Company ABC has a WACC of 11.2%, a cost of equity of 14%, and a cost of debt
of 5%. What is ABC’s debt-equity ratio?
- 33.3%
- ✓ 45%
- 75%
- 85%

    11.2 = 14 * E/V + 5% (1-E / V)

    some magic: E/V = 69% => D/V = 31% => D/E = 31/69 = 45%

    D/E = 45%

9 The total market value of the company stock of XYZ Real Estate Company is $6 million, and the total value of its debt is $4 million. The treasurer estimates that the beta of the stock is currently 1.5 and that the expected risk premium on the market is 9%. The Treasury bill rate is 8%. Assume the company’s cost of debt equals the risk free rate. Estimate the company’s cost of capital.
- 15.2%
- ✓ 16.1%
- 21.5%
- 24%

    E           = 6m
    D           = 4m
    r.f.        = 8%
    B           = 1.5
    eq prem     = 9%
    qual spread =
    tc          =

    E / (D + E) = 6 / 10 = 60%
    D / (D + E) = 4 / 10 = 40%

    Re = r.f. + B * eq prem
       = 8 + 1.5 * 9
       = 21.5%

    Rd = r.f. + qual sp
       = 8 +
       =

    WACC = 60 * 21.5 + 40 * 8
         = 1290 + 320
         = 16.1%

10 Suppose XYZ Real Estate Company now wants to produce computers. The average
beta of unlevered computer manufacturers is 1.2. Estimate the required return
on XYZ’s new venture.
- ✓ 14.5%
- 16.1%
- 18.8%
- 21.5%

    E / D+E = 60%
    D / D+E = 40%

    Re = 8 + 1.2 * 9 = 18.8

    Rd = 8

    WACC = 60 * 18.8 + 40 * 8 = 14.5


### QUIZ

1 Stock A has a beta of 0.8, whereas stock B has a beta of 1.5. Which one of
these stocks would you recommend to a very risk-averse investor?
- ✓ Stock A
- Stock B

2 What is the beta of the market portfolio?
- 0.0
- 0.5
- ✓ 1.0

3 Firm A has a debt-equity ratio of 100%, whereas firm B has a debt-equity
ratio of 10%. Suppose A and B are identical in all other aspects. Which one
should have a higher beta?
- ✓ Firm A
- Firm B

    100% => D = 100, E = 1
    10%  => D = 10, E = 100

4 Company XYZ has a beta of 1.5. Assume the Treasury bond rate is 7%, and the
risk premium is 9.5%. What is the expected return on XYZ’s stock?
- ✓ 21.25%
- 13.65%
- 31.8%
- 8.5%

    B = 1.5
    r.f. = 7%
    eq prem = 9.5%

    Re = r.f. + B * eq prem
        = 7 + 1.5 * 9.5
        = 21.25

5 A stock has an expected return of 10.2%, the risk-free rate is 4%, and the
market risk premium is 7%. What must be the beta of this stock?
- 0.85
- 0.75
- ✓ 0.89
- 1.12

    10.2 = 4 + B * 7
    6.2 = B * 7
    B = 0.885

6 Company XYZ has a target capital structure of 50% equity and 50% debt. Its
cost of equity is 10%, and cost of debt is 5%. Suppose there is no tax. Should
the company take on a project that demands an initial investment of $500
million, and provides an income of $600 million in 2 years?
- ✓ Yes
- No

    WACC = 50/100 * 10 + 50/100 * 5 = 5 + 2.5 = 7.5


    FV = PV * (1 + r)^t
        = 500 * (1 + 7.5)^2 = 577m

7 In the above example, what if the income of $600 million comes in 3 years?
- Yes
- ✓ No

8 A company has 25% of its assets financed by debt. What is this company’s
debt-equity ratio?
- 100%
- 75%
- 66.6%
- ✓ 33.3%

    E = 1 - D
      = 1 - 25% = 75%

    D/E = 25/75 = 33.3

9 A company has a debt-equity ratio of 50%. How much of this company’s assets
are financed by equity?
- 66.6%
- 50%
- 25%
- 10%

    D/E = 50 => D = 50, E = 100

    E / D+E = 100/150 = 66.6%

10 Company FIN has a WACC of 9.8%, a cost of equity of 13%, and a cost of debt
of 6.5%. What is FIN’s debt-equity ratio?
- ✓ 97%
- 100%
- 90%
- 85%

    ! No fucking clue

    Ans from quiz: 9.8%=13%*E/V + 6.5%*(1-E/V) => E/V = 50.77% => D/E = 97%
## WEEK 5: CAPSTONE CASE: SUNRISE BAKERY EXPANSION

### BACKGROUND ON THE CASE (Original text)

Background on the Case

The Sunrise Bakery Corporation was originally founded in Houston, TX in 1991 by
Griffin Harris, who currently serves as the company's Chief Executive Officer.
About four years ago, Griffin's daughter, Erica, moved into the company to
serve as Chief Financial Officer. Erica had graduated from college a few years
ago and had worked for a few years in retail. However, for the past two years,
she had been working quite successfully on an online accounting degree, but she
still felt a little uncomfortable in her new role as CFO of the family
business.

Sunrise produces and markets a variety of bakery products throughout southeast
Texas and Louisiana. They operate mostly through warehouse delivery and produce
fresh breads, buns, rolls, and snack cakes under a few of their own regional
brands but also including some licensed "big name" national brands. In total,
they operate five bakeries with one very large facility and four smaller
production sites. For the past three years, sales have averaged about $15
Million, generating about $650 Thousand in Net Income per year. However, sales
have been roughly flat for the past six years as growth has slowed and
production capacity has reached nearly 100%. In order to grow sales, Sunrise
Bakery needs to invest in further production capacity.

Griffin Harris has been looking to purchase more space, build additional
bakeries, or even perhaps acquire one of their smaller competitors, but nothing
specific has worked out yet. Erica has an alternative short-term plan to
modernize the production process at their main plant. Her idea involves the
purchase of a new, significantly faster, integrated commercial oven that she
recently saw displayed at a trade show. Few other bakeries in the region have
invested in this modern equipment, and she expects it may cut costs and improve
output efficiency. Her sales representative suggests the new oven *could raise
incremental sales at their large bakery by 15%*.

Installation of the oven could be mostly executed over the upcoming Labor-day
long weekend and shouldn't disrupt sales or production too much. However, the
new oven requires an expenditure of $350,000, which would be a large capital
expenditure for Sunrise. To reflect the wear and tear on the oven, *tax law
allows for a 10% annual reduction in the value of the oven as a depreciation
expense*. That is, Erica’s financial forecast includes a non-cash expense of
*$35,000 for each of the next six years*. After six years, Erica’s sales
representative expects the oven to be worth about *$140,000*, which is just equal
to the accounting book value of the oven after six years of accumulated
depreciation ($140,000 = $350,000 – 6 * 10% * $350,000).

Operation of the oven also requires a small initial investment in an inventory
of spare parts of $15,000. The inventory should be fully recoverable for
$15,000 if the machine is sold. The investment in inventory represents an
increase in other current assets (inventory) that should be included as a
change in working capital requirements for Sunrise Bakery. Sunrise estimates
receivables at 1.5% of revenues and payables at 2% of revenues each year. A the
end of the project, Erica expects to recover all of the working capital
invested in the project. In other words, she expects a cash flow equal to the
amount of Non-Cash Current Assets less Current Liabilities in the last year of
the project.

Erica’s financial forecast for the new oven does not require any significant
change in financing. Sunrise started with one small bakery entirely paid for
with cash from Griffin Harris and a mortgage on the bakery property. Currently,
Sunrise maintains a rough capital structure of about 25% debt and 75% equity.
In Erica's forecast, she expects to purchase the new oven with available cash
and retained earnings (Sunrise's own money) and without any additional drawdown
on their bank line of credit (no new debt). Sunrise currently pays about 4.5%
on their debt, and that rate is not expected to change with the additional
purchase of the oven. No additional external financing should be needed, and
after discussions with her loan office, Erica expects the bank will approve the
purchase of the oven without any effect on their line of credit. Overall, the
cash purchase of the oven is not expected to change the capital structure of
the Sunrise Corporation. However, since the oven will become part of the assets
of Sunrise, the bank could seize the oven should Sunrise fail to make payments
on their current debt.

Erica remembered from her online classes that she needs to assess the risk of
her business when making important financial decisions. In researching similar
large public bakery and other food manufacturers, she found that firms in her
industry with about the same level of risk mostly had stock market betas around
0.80 on average. She also noted that many analysts used a ballpark equity risk
premium of 5.5% and a current yield on U.S. treasury bonds (risk-free rate) of
about 3%. Sunrise has a corporate tax rate of 30%.

To help understand the costs and benefits of the decision, Erica worked closely
with her director of operations, plant manager, marketing team, and her father
to produce some realistic sales, costs, and financial forecasts. Her team felt
uncomfortable forecasting more than 5 or 6 years into the future. Her focus was
on how the new oven might improve incremental revenue generation at their large
plant. The case exhibits below contain Erica's financial projections for the
project.

In discussing her plan to purchase the new oven, Erica's father seems more than
a little worried that the new machinery is not worth the cost and that Erica's
motivations may not be based on sound financial decision making. As Erica
looked over the financial forecasts, market data, line of credit agreement, and
the intimidating $350,000 invoice that would soon follow, she wondered how she
could convince her father, and herself, that purchasing the new oven would be a
sound financial decision.

### BACKGROUND: MY NOTES

5 bakeries
- 1 large
- 4 smaller

Sales last 3 years
- avg `$15M`
- `$650K` Net Income per year
- sales flat past 6 years

Production Capacity
- reached nearly `100%`

Need to invest in production capacity to grow sales
- New efficient ovens could raise incremental sales `15%`
- expenditure $350K
- Tax depreciation 10% => non-cash expense of $35K/yr
  - 6 yr deprec `$140K` = 350K - 6 * 10% * 350K
- OpX = initial 15K which should be recoverable if sold
- receivables 1.5% of revenues per year
- payables 2% of revenues per year
- expect to recover all working capital invested at end of project
  - => cash flow == Non-Cash Current Assets - Current Liabilities
- Capital Structure == 25% Debt, 75% Equity
- Shouldn't require new debt to purchase
- Currently paying 4.5% on debt
- firms in indstry =~ 0.80 beta
- ballpark equity risk premium 5.5%
- US Bonds 3%
= Sunrise corp tax 30%

[Use the Sunrise Bakery spreadsheet](https://docs.google.com/spreadsheets/d/1yA58Dro_9i8wRFRNT0XglMQdj8qjiQ5OPF6tpNabXZA/edit#gid=1209642017)

#### WORKSHEET

**1 What is the cost of debt for Sunrise Bakery?**

Rd 4.5% (given)

**2 What is their cost of equity?**

7.4% == Risk Free Rate + (Beta * Equity Risk Premium)

**3 What is the WACC?**

    WACC = ( E / (E + D) * Re ) + ( (D / E+D) * (1-tc) * Rd )

Given: 
- Capital Structure == 25% Debt, 75% Equity
- Tax depreciation 10% 

    WACC = 75% * 7.4% + 25% * (1 - 10%) * 4.5%
         = 6.34%

**4 Which cost of capital should be used to evaluate the feasibility of the oven purchase?**

    WACC = 6.34%

**5 Calculate the annual depreciation expense for sunrise capital .**

    35K
    
**6 What is the after-tax net income in each of the six years?**

See Row 21

**7 Calculate the change in working capital each year from the projected financial statements.**

    Working Capital = Current Assets (Row 27) - Curr Liabailities (row 36)

See Row 41

**8 What is the terminal value of the project at the end of year 6?**

    140K

See Row 48

**9 Compute the free cash flows for each year.**

     FCF = Operating Profit (after tax)
         – Increase in WC (Working Capital)
         + Depreciation
         – Capital expenditure
         + After tax salvage value

Row 49

**10 What is the IRR?**

Row 54 == `22.97%`

**11 Calculate the NPV.**

Row 58 = `240982`

**12 Using Payback Analysis, how many years until the project pays off the investment?**

Row 60 == `5`

**13 What is the return on invested capital?**

Row 65 = `27.4%`

**14 Should Sunrise Bakery purchase the new oven?**

Yes

### FINAL EXAM

[See Final Exam.pdf](https://drive.google.com/drive/folders/0BwjXv3TJiWYEVHo0ci00RlJrbUk)
