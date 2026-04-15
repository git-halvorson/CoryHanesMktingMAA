#!/usr/bin/env python3
"""Generate all 6 Insights Hub article pages."""
import os

BRAND_CSS = """
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600;700&family=Cormorant:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&display=swap" rel="stylesheet">
  <style>
    *,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
    :root{
      --navy:#0A1628;--navy-700:#0e2040;--navy-600:#163460;
      --gold:#D97706;--gold-light:#FDE68A;
      --slate:#334155;--slate-light:#64748B;--slate-border:#E2E8F0;
      --max:740px;
    }
    html{font-size:17px;-webkit-font-smoothing:antialiased}
    body{font-family:'IBM Plex Sans',sans-serif;color:var(--navy);background:#F8FAFC;line-height:1.7}

    /* ── NAV ── */
    nav{background:var(--navy);position:sticky;top:0;z-index:50;border-bottom:1px solid rgba(255,255,255,.07)}
    .nav-inner{max-width:1120px;margin:0 auto;padding:0 24px;display:flex;align-items:center;justify-content:space-between;height:56px}
    .nav-logo{display:flex;align-items:center;gap:10px;text-decoration:none}
    .nav-logo-mark{width:28px;height:28px;background:#1E3A8A;border-radius:4px;display:flex;align-items:center;justify-content:center}
    .nav-logo-text{font-family:'IBM Plex Sans',sans-serif;font-size:13px;font-weight:600;color:#fff;letter-spacing:.02em}
    .nav-back{font-size:13px;color:rgba(255,255,255,.55);text-decoration:none;display:flex;align-items:center;gap:6px;transition:color .2s}
    .nav-back:hover{color:#FBBF24}
    .nav-back svg{opacity:.7}
    .nav-cta{background:#D97706;color:#fff;font-size:12px;font-weight:600;padding:7px 16px;border-radius:6px;text-decoration:none;transition:background .2s}
    .nav-cta:hover{background:#B45309}

    /* ── HERO ── */
    .article-hero{background:var(--navy);padding:56px 24px 52px}
    .article-hero-inner{max-width:var(--max);margin:0 auto}
    .tag{display:inline-block;font-size:11px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;padding:3px 10px;border-radius:99px;margin-bottom:18px}
    .tag-exit{background:rgba(20,184,166,.15);color:#2DD4BF}
    .tag-valuation{background:rgba(245,158,11,.15);color:#FCD34D}
    .tag-sell{background:rgba(59,130,246,.15);color:#93C5FD}
    .tag-deal{background:rgba(168,85,247,.15);color:#D8B4FE}
    .tag-mkt{background:rgba(244,63,94,.15);color:#FDA4AF}
    .article-hero h1{font-family:'Cormorant',serif;font-size:clamp(32px,5vw,48px);font-weight:600;color:#fff;line-height:1.12;margin-bottom:20px;letter-spacing:-.01em}
    .article-meta{display:flex;flex-wrap:wrap;align-items:center;gap:16px;font-size:13px;color:rgba(255,255,255,.45)}
    .article-meta .author{display:flex;align-items:center;gap:8px;color:rgba(255,255,255,.65)}
    .author-avatar{width:28px;height:28px;border-radius:50%;background:linear-gradient(135deg,#1E3A8A,#D97706);display:flex;align-items:center;justify-content:center;font-size:10px;font-weight:700;color:#fff;flex-shrink:0}
    .meta-sep{opacity:.3}

    /* ── BODY ── */
    .article-body{max-width:var(--max);margin:0 auto;padding:52px 24px 80px}
    .article-body p{margin-bottom:22px;color:var(--slate);font-size:1rem;line-height:1.75}
    .article-body h2{font-family:'Cormorant',serif;font-size:clamp(22px,3vw,28px);font-weight:600;color:var(--navy);margin:40px 0 14px;line-height:1.2}
    .article-body h3{font-size:16px;font-weight:600;color:var(--navy);margin:28px 0 10px}
    .article-body ul,.article-body ol{margin:0 0 22px 0;padding-left:22px;color:var(--slate)}
    .article-body li{margin-bottom:8px;line-height:1.65}
    .article-body strong{color:var(--navy);font-weight:600}
    .callout{background:#FFF7ED;border-left:3px solid var(--gold);padding:18px 22px;border-radius:0 8px 8px 0;margin:28px 0;font-size:.95rem;color:#78350F}
    .callout strong{color:#92400E}
    .data-table{width:100%;border-collapse:collapse;margin:28px 0;font-size:.875rem}
    .data-table th{background:var(--navy);color:#fff;padding:10px 14px;text-align:left;font-weight:500;font-size:.8rem;letter-spacing:.04em;text-transform:uppercase}
    .data-table td{padding:10px 14px;border-bottom:1px solid var(--slate-border);color:var(--slate)}
    .data-table tr:last-child td{border-bottom:none}
    .data-table tr:nth-child(even) td{background:#F8FAFC}
    .highlight{background:#EFF6FF;border-radius:8px;padding:20px 24px;margin:28px 0;border:1px solid #BFDBFE}
    .highlight p{margin:0;color:#1E40AF;font-size:.95rem}

    /* ── CTA BOX ── */
    .cta-box{background:var(--navy);border-radius:12px;padding:36px 32px;margin:48px 0 0;text-align:center}
    .cta-box h3{font-family:'Cormorant',serif;color:#fff;font-size:26px;font-weight:600;margin-bottom:10px}
    .cta-box p{color:rgba(255,255,255,.55);font-size:.9rem;margin-bottom:22px}
    .btn-gold{display:inline-block;background:var(--gold);color:#fff;font-size:14px;font-weight:600;padding:12px 28px;border-radius:6px;text-decoration:none;transition:background .2s}
    .btn-gold:hover{background:#B45309}
    .btn-outline-white{display:inline-block;border:1px solid rgba(255,255,255,.25);color:rgba(255,255,255,.7);font-size:13px;font-weight:500;padding:11px 24px;border-radius:6px;text-decoration:none;transition:all .2s;margin-left:12px}
    .btn-outline-white:hover{border-color:rgba(255,255,255,.6);color:#fff}

    /* ── FOOTER ── */
    footer{background:var(--navy);border-top:1px solid rgba(255,255,255,.07);padding:32px 24px;text-align:center}
    footer p{font-size:12px;color:rgba(255,255,255,.3)}
    footer a{color:rgba(255,255,255,.45);text-decoration:none}
    footer a:hover{color:#FBBF24}
  </style>
"""

NAV = """<nav>
  <div class="nav-inner">
    <a class="nav-logo" href="../index.html">
      <div class="nav-logo-mark">
        <svg width="16" height="16" viewBox="0 0 36 36" fill="none"><path d="M7 26V12l5.5 7.5L18 12l5.5 7.5V26M24 12v14h5" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </div>
      <span class="nav-logo-text">Mid Mkt Advisors</span>
    </a>
    <a class="nav-back" href="../index.html#blog">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M19 12H5M12 5l-7 7 7 7"/></svg>
      All Articles
    </a>
    <a class="nav-cta" href="../index.html#schedule">Get a Free Valuation</a>
  </div>
</nav>"""

FOOTER = """<footer>
  <p>&copy; 2026 Mid Mkt Advisors &mdash; Horizon M&A Advisors &nbsp;&middot;&nbsp;
    <a href="../index.html">Home</a> &nbsp;&middot;&nbsp;
    <a href="../index.html#blog">Insights</a> &nbsp;&middot;&nbsp;
    <a href="mailto:dave@horizonmaa.com">dave@horizonmaa.com</a> &nbsp;&middot;&nbsp;
    <a href="tel:+14083985553">408-398-5553</a>
  </p>
</footer>"""

CTA = """<div class="cta-box">
  <h3>Ready to Explore Your Options?</h3>
  <p>Get a confidential, no-obligation valuation assessment from David Halvorson &mdash; 500+ closed transactions, senior-led from first call to close.</p>
  <a class="btn-gold" href="../index.html#schedule">Schedule a Free Consultation</a>
  <a class="btn-outline-white" href="../index.html#blog">More Articles</a>
</div>"""

def page(title, meta_desc, tag_class, tag_label, pub_date, read_time, body_html, slug):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Mid Mkt Advisors</title>
  <meta name="description" content="{meta_desc}">
{BRAND_CSS}
</head>
<body>
{NAV}
<header class="article-hero">
  <div class="article-hero-inner">
    <span class="tag {tag_class}">{tag_label}</span>
    <h1>{title}</h1>
    <div class="article-meta">
      <span class="author">
        <span class="author-avatar">DH</span>
        David Halvorson
      </span>
      <span class="meta-sep">&middot;</span>
      <span>{pub_date}</span>
      <span class="meta-sep">&middot;</span>
      <span>{read_time}</span>
    </div>
  </div>
</header>
<main class="article-body">
{body_html}
{CTA}
</main>
{FOOTER}
</body>
</html>"""

# ── ARTICLES ──────────────────────────────────────────────────────────────────

articles = []

# 1. Exit Readiness Checklist
articles.append(('exit-readiness-checklist.html', page(
    title="How to Prepare Your Business for a Sale: The 12-Month Exit Readiness Checklist",
    meta_desc="The exact 12-month preparation timeline Mid Mkt Advisors uses before approaching a single buyer — from EBITDA normalization to eliminating key person risk.",
    tag_class="tag-exit", tag_label="Exit Planning",
    pub_date="April 14, 2026", read_time="9 min read",
    slug="exit-readiness-checklist",
    body_html="""
<p>Most founders who go to market unprepared leave 20&ndash;40% of their business value on the table. Not because their business isn't valuable &mdash; it is. But because buyers are professional negotiators who have done hundreds of deals, and they know exactly which weaknesses to find and exploit.</p>
<p>The preparation work we do in the 12 months before a sale is where most of the premium gets built. Here's the exact framework we use with every client.</p>

<h2>Months 12&ndash;9: Financial Foundation</h2>
<h3>Normalize Your EBITDA</h3>
<p>Buyers will scrutinize three years of financials. Before they do, you need to present those financials in the most favorable &mdash; and defensible &mdash; light. That means building a proper add-back schedule: every one-time expense, above-market owner compensation, personal items run through the business, and non-recurring costs that won't continue post-close.</p>
<p>Common legitimate add-backs include owner life insurance premiums, personal vehicles, above-market officer salaries, one-time legal or accounting fees, and non-recurring capex. Each must be documented and verifiable.</p>
<div class="callout"><strong>Rule of thumb:</strong> Every $100K of defensible EBITDA add-back is worth $500K&ndash;$700K in deal value at a 5&ndash;7x multiple. This is where the prep work pays for itself.</div>

<h3>Upgrade Your Financial Reporting</h3>
<p>If you're on cash-basis accounting, convert to accrual. If your books are in QuickBooks and haven't been reviewed by a CPA, get reviewed financials at minimum &mdash; audited if your revenue is above $30M. Buyers at the institutional level expect clean, professional financials. Anything less signals risk and becomes a price chip.</p>

<h2>Months 9&ndash;6: Operational Readiness</h2>
<h3>Reduce Owner Dependency</h3>
<p>The single biggest valuation discount in the lower middle market is key person risk: the perception that the business can't run without you. Buyers will ask directly: "If you left tomorrow, what would happen?" If the honest answer is "a lot would break," you have work to do.</p>
<p>The fix isn't complicated but it takes time: document processes, elevate your #2, introduce that person to key customers and suppliers, and give them visible operational authority. Buyers need to see a business, not a job.</p>

<h3>Clean Up Customer Concentration</h3>
<p>If any single customer represents more than 20% of revenue, buyers will discount for that risk &mdash; or walk. If your top customer is 30%+ of revenue, start the diversification work now. Even moving from 30% to 22% materially changes the risk conversation.</p>

<h2>Months 6&ndash;3: Transaction Readiness</h2>
<h3>Organize Your Data Room</h3>
<p>A data room is where deals go to die if it's not ready. Build it before you need it. Standard items include: three years of financial statements, tax returns, customer contracts, employee agreements and org chart, lease agreements, equipment list, any IP documentation, and a list of material contracts. Having this organized signals professionalism and shortens due diligence timelines.</p>

<h3>Resolve Pending Legal and HR Issues</h3>
<p>Any unresolved litigation, environmental issues, HR complaints, or regulatory matters will surface in due diligence and become price adjustments or deal killers. Address them now while you control the narrative.</p>

<table class="data-table">
  <thead><tr><th>Area</th><th>Red Flag</th><th>Fix It Now</th></tr></thead>
  <tbody>
    <tr><td>Financials</td><td>Cash-basis, no CPA review</td><td>Accrual conversion + reviewed statements</td></tr>
    <tr><td>Customer base</td><td>Any customer &gt;20% of revenue</td><td>Active diversification program</td></tr>
    <tr><td>Management</td><td>No #2 who could run operations</td><td>Identify, elevate, document</td></tr>
    <tr><td>Contracts</td><td>Month-to-month customer agreements</td><td>Multi-year contracts where possible</td></tr>
    <tr><td>Legal</td><td>Open litigation or HR issues</td><td>Resolve or disclose early</td></tr>
    <tr><td>Data room</td><td>Disorganized or incomplete</td><td>Build the full room before launch</td></tr>
  </tbody>
</table>

<h2>Months 3&ndash;0: Go-to-Market Prep</h2>
<p>This is when your advisor builds the Confidential Information Memorandum (CIM), develops the buyer list, and prepares the financial model. Your role here is to be responsive and to stay out of the business details long enough to support the process &mdash; which means your operational team needs to be running things without you in the loop for every decision.</p>
<div class="highlight"><p><strong>The bottom line:</strong> Businesses that go to market prepared sell faster, attract more serious buyers, and close 20&ndash;35% higher than unprepared peers. The 12 months before a sale are the highest-leverage months of the entire exit process.</p></div>
""")))

# 2. EBITDA Multiples Q1 2026
articles.append(('ebitda-multiples-q1-2026.html', page(
    title="EBITDA Multiples in the Lower Middle Market: Q1 2026 Report",
    meta_desc="Current EBITDA multiple ranges by sector in the lower middle market. What's driving compression in services and expansion in technology-enabled businesses.",
    tag_class="tag-valuation", tag_label="Valuation",
    pub_date="April 11, 2026", read_time="7 min read",
    slug="ebitda-multiples-q1-2026",
    body_html="""
<p>Valuation multiples in the lower middle market (&dollar;2M&ndash;&dollar;15M EBITDA) are not uniform &mdash; they vary significantly by sector, growth profile, revenue quality, and deal structure. Understanding where your business falls in the range is the first step to a realistic exit strategy.</p>
<p>Here's what we're seeing in Q1 2026, drawn from active deal activity across our platform and buyer network.</p>

<h2>Current Multiple Ranges by Sector</h2>
<table class="data-table">
  <thead><tr><th>Sector</th><th>Base Range</th><th>Premium Range</th><th>Direction</th></tr></thead>
  <tbody>
    <tr><td>Technology-Enabled Services</td><td>7&ndash;9x</td><td>10&ndash;13x</td><td>&#8593; Expanding</td></tr>
    <tr><td>Healthcare Services</td><td>6&ndash;8x</td><td>9&ndash;11x</td><td>&#8594; Stable</td></tr>
    <tr><td>IT Managed Services / MSP</td><td>6&ndash;8x</td><td>9&ndash;12x</td><td>&#8593; Expanding</td></tr>
    <tr><td>Specialty Manufacturing</td><td>5&ndash;7x</td><td>7&ndash;9x</td><td>&#8594; Stable</td></tr>
    <tr><td>Business Services</td><td>5&ndash;7x</td><td>7&ndash;9x</td><td>&#8595; Compressing</td></tr>
    <tr><td>Distribution / Logistics</td><td>4&ndash;6x</td><td>6&ndash;8x</td><td>&#8595; Compressing</td></tr>
    <tr><td>Specialty Contracting</td><td>4&ndash;6x</td><td>6&ndash;8x</td><td>&#8594; Stable</td></tr>
    <tr><td>General Contracting</td><td>3&ndash;5x</td><td>5&ndash;7x</td><td>&#8595; Compressing</td></tr>
  </tbody>
</table>

<h2>What's Driving the Divergence</h2>
<h3>Technology Premium Is Accelerating</h3>
<p>Businesses with recurring software revenue, proprietary technology, or AI-assisted service delivery are commanding a meaningful premium over comparable human-capital-intensive businesses. A distribution company with a proprietary routing and inventory platform is valued differently than a traditional distributor &mdash; even at the same EBITDA level.</p>
<p>PE firms are specifically targeting "technology-enabled" add-ons for their platform companies. If your business has any tech component, make sure your CIM tells that story clearly.</p>

<h3>Services Compression Is Real</h3>
<p>General business services businesses with undifferentiated offerings and high labor dependency are seeing multiple compression. The culprits: labor cost inflation has reduced margins, making normalized EBITDA harder to defend; buyer competition for these assets has softened; and PE platforms have gotten more selective after overpaying for services roll-ups in 2021&ndash;2022.</p>

<h3>The Quality Premium Matters More Than Ever</h3>
<div class="callout"><strong>Key finding:</strong> The spread between "average quality" and "premium quality" businesses in the same sector has widened to 2&ndash;3x turns in most categories. Quality factors &mdash; revenue predictability, customer concentration, management depth &mdash; now move the needle more than sector selection alone.</div>

<h2>What Moves You Toward the Premium Range</h2>
<ul>
  <li><strong>Recurring / contracted revenue</strong> &mdash; MRR, ARR, long-term contracts signal predictability</li>
  <li><strong>Low customer concentration</strong> &mdash; No customer &gt; 10&ndash;15% of revenue is ideal</li>
  <li><strong>Management depth</strong> &mdash; A team that can run the business post-close</li>
  <li><strong>Organic growth</strong> &mdash; 10%+ CAGR over three years signals market position</li>
  <li><strong>Gross margin expansion</strong> &mdash; Improving margins suggest pricing power and operational leverage</li>
  <li><strong>Clean data room</strong> &mdash; Organized, audit-ready financials reduce perceived risk</li>
</ul>

<h2>The Process Premium</h2>
<p>Multiple ranges above represent what a well-run competitive process achieves. Single-buyer negotiations &mdash; where a founder accepts the first serious offer or deals with one strategic buyer &mdash; typically close at 1&ndash;2 turns below market. The process creates the tension that moves buyers toward the top of their range.</p>
<div class="highlight"><p><strong>Bottom line:</strong> Sector matters, but quality and process matter more. A well-prepared business in a compressing sector, taken through a structured competitive process, will consistently outperform an average business in a hot sector sold quietly to a single buyer.</p></div>
""")))

# 3. Competitive Process
articles.append(('competitive-process.html', page(
    title="Why 80% of Business Owners Leave Money on the Table Without a Competitive Process",
    meta_desc="Single-buyer negotiations almost always underperform. The data from 500+ transactions on what a structured competitive process delivers and why it matters more than the headline multiple.",
    tag_class="tag-sell", tag_label="Sell-Side",
    pub_date="April 8, 2026", read_time="6 min read",
    slug="competitive-process",
    body_html="""
<p>When a founder tells me they have "a buyer ready to go" before they've engaged an advisor, I always say the same thing: "That buyer isn't ready to go &mdash; they're ready to negotiate."</p>
<p>The most expensive mistake in M&A is confusing a willing buyer with a fair price. Here's the data on why competitive processes consistently outperform single-buyer deals.</p>

<h2>The Numbers Don't Lie</h2>
<p>Across 500+ closed transactions, businesses sold through a structured, multi-buyer process consistently close at 15&ndash;30% higher valuations than comparable businesses sold through a single-buyer negotiation. That's not a slight edge &mdash; at a $20M business, 20% is $4M walking out the door.</p>
<div class="callout"><strong>Example:</strong> A $3M EBITDA IT services business sold in a single-buyer negotiation at 6x = $18M. The same business, taken through a competitive process with 8&ndash;12 qualified buyers, typically generates LOIs at 7.5&ndash;8.5x = $22.5M&ndash;$25.5M. The process premium is real and predictable.</div>

<h2>Why Single-Buyer Deals Underperform</h2>
<h3>1. You're Negotiating With No Leverage</h3>
<p>In a single-buyer negotiation, the buyer knows they're the only game in town. They have unlimited time to tire you out, uncover weaknesses in due diligence, and renegotiate at the LOI stage. Every data room request is also a negotiating tactic. You have no credible alternative, so you concede.</p>

<h3>2. You Don't Know Market Value</h3>
<p>Without running a process, you don't know what the market will pay. The first buyer's offer feels like "market" because you have nothing to compare it to. In reality, it's a starting negotiating position &mdash; designed to leave room to move only if you push back, which most founders don't.</p>

<h3>3. Buyers Compete for Price Only When They Have To</h3>
<p>PE firms and strategic acquirers have deal teams whose full-time job is to acquire companies at the best possible price. They know that a seller without a process has no leverage. When they know there are competing LOIs on the table, behavior changes immediately: decision timelines compress, pricing moves up, and terms improve.</p>

<h2>What a Competitive Process Looks Like</h2>
<ol>
  <li><strong>Prepare the CIM and financial model</strong> &mdash; 4&ndash;6 weeks of preparation before approaching a single buyer</li>
  <li><strong>Build the buyer list</strong> &mdash; 30&ndash;80 qualified buyers across PE, strategic, and family office categories</li>
  <li><strong>Controlled outreach</strong> &mdash; Confidential, NDA-gated introductions with deadline-driven process letters</li>
  <li><strong>Management presentations</strong> &mdash; Final-round buyers present their vision; sellers evaluate fit and culture</li>
  <li><strong>LOI deadline</strong> &mdash; All final-round buyers submit offers by the same date, creating genuine competition</li>
  <li><strong>Negotiate from strength</strong> &mdash; With multiple LOIs in hand, you negotiate toward the best combined outcome: price + terms + fit</li>
</ol>

<h2>It's Not Just About Price</h2>
<p>A competitive process improves more than the headline number. With multiple buyers competing, you also get:</p>
<ul>
  <li><strong>Better deal structure</strong> &mdash; Less seller note, lower earnout risk, cleaner working capital peg</li>
  <li><strong>Better terms</strong> &mdash; Shorter indemnification periods, lower escrow holdbacks, broader reps &amp; warranties coverage</li>
  <li><strong>Better fit</strong> &mdash; You can choose the buyer who is the right home for your employees and customers, not just the one who showed up</li>
  <li><strong>Faster close</strong> &mdash; Competitive pressure shortens timelines; deals with leverage close faster</li>
</ul>
<div class="highlight"><p><strong>The bottom line:</strong> A well-run competitive process is the single highest-leverage thing you can do to maximize the outcome of a sale you've spent 20&ndash;30 years building toward. The preparation takes time, but it pays for itself many times over.</p></div>
""")))

# 4. SBA vs Conventional
articles.append(('sba-vs-conventional-financing.html', page(
    title="SBA vs. Conventional Financing: What Every Seller Needs to Know About Their Buyer's Capital Stack",
    meta_desc="When your buyer uses SBA 7(a) financing, deal mechanics change dramatically. Price, timing, holdbacks, and seller note structure all shift. Here's what to expect and how to protect yourself.",
    tag_class="tag-deal", tag_label="Deal Structure",
    pub_date="April 5, 2026", read_time="8 min read",
    slug="sba-vs-conventional-financing",
    body_html="""
<p>When you receive an LOI, the headline price matters &mdash; but so does what's behind it. Whether your buyer is using SBA 7(a) financing or conventional (non-SBA) debt changes the deal mechanics in ways that affect your net proceeds, your timeline, and your ongoing risk exposure.</p>
<p>Here's what you need to know before you sign an LOI from a buyer using SBA financing.</p>

<h2>The Basics: How Each Works</h2>
<table class="data-table">
  <thead><tr><th>Factor</th><th>SBA 7(a)</th><th>Conventional / PE</th></tr></thead>
  <tbody>
    <tr><td>Maximum loan size</td><td>$5M (SBA guaranteed)</td><td>No statutory limit</td></tr>
    <tr><td>Typical deal size</td><td>Under $15M enterprise value</td><td>$10M+ (no ceiling)</td></tr>
    <tr><td>Equity requirement</td><td>10&ndash;15% buyer equity</td><td>30&ndash;50% PE equity</td></tr>
    <tr><td>Seller note requirement</td><td>Often required (10%)</td><td>Negotiated, often none</td></tr>
    <tr><td>Close timeline</td><td>60&ndash;90 days (bank-dependent)</td><td>45&ndash;75 days</td></tr>
    <tr><td>Standby period on seller note</td><td>24 months mandatory</td><td>Negotiated</td></tr>
  </tbody>
</table>

<h2>The Seller Note Issue</h2>
<p>SBA lenders frequently require the seller to carry a note &mdash; typically 10% of the purchase price &mdash; as a condition of approving the loan. This is a meaningful distinction from conventional deals. In an SBA transaction, your seller note is often placed on "standby" for 24 months post-close, meaning you cannot receive payments on it while the SBA loan is in its early phase.</p>
<div class="callout"><strong>What this means for you:</strong> On a $10M deal with a 10% seller note, you have $1M that you cannot touch for two years post-close &mdash; and if the buyer defaults on the SBA loan, your ability to collect on that note is subordinated to the SBA's recovery. This is a real risk, not a theoretical one.</div>

<h2>How It Affects Price</h2>
<p>SBA buyers often bid higher headline prices because their personal equity requirement is lower (10&ndash;15% vs. 30&ndash;50% for PE). A buyer putting $1.5M down can bid $10M with SBA financing &mdash; the same buyer without SBA access might only be able to offer $5M conventionally.</p>
<p>This creates a nuanced tradeoff: the SBA buyer may have the highest headline offer, but the actual structure (seller note, standby, closing risk) may make a lower all-cash PE offer more valuable in net present value terms.</p>

<h2>The Closing Risk Difference</h2>
<p>SBA loans have a meaningful failure rate at the conditional approval stage. Bank underwriting standards, SBA guarantee requirements, and third-party appraisal requirements (the SBA requires an independent business valuation) all create friction that conventional deals don't have.</p>
<p>In a conventional PE or institutional deal, if the buyer has committed equity and a lender in place, closing risk is lower. The process is faster, the conditionality is narrower, and there are fewer third parties who can slow or kill the deal.</p>

<h2>What to Negotiate If You Take an SBA Offer</h2>
<ul>
  <li><strong>Minimize the seller note.</strong> Push to eliminate it or reduce to the SBA minimum. Every dollar in the seller note is a dollar at risk.</li>
  <li><strong>Shorten the standby period.</strong> SBA rules set a 24-month floor, but negotiate any payments you can outside the standby structure.</li>
  <li><strong>Require a deposit at LOI.</strong> Non-refundable deposits (even $25&ndash;50K) screen out tire-kickers and signal buyer seriousness.</li>
  <li><strong>Cap the due diligence period.</strong> SBA transactions have more moving pieces; build a hard timeline into the LOI.</li>
  <li><strong>Require business valuation in advance.</strong> SBA appraisals sometimes come in below the agreed price, triggering renegotiation. Ask to see the appraisal methodology before signing.</li>
</ul>
<div class="highlight"><p><strong>Bottom line:</strong> SBA financing is not inherently bad for sellers &mdash; it enables buyers who couldn't otherwise participate, which increases buyer pool and competition. But the deal structure is different and requires specific protections. Evaluate total net proceeds and risk, not just the headline number.</p></div>
""")))

# 5. Key Person Risk
articles.append(('key-person-risk.html', page(
    title="Key Person Risk: The Single Biggest Valuation Discount Most Founders Don't See Coming",
    meta_desc="If your business can't run without you, buyers know it and price it accordingly. A practical framework for reducing owner dependency before you go to market.",
    tag_class="tag-exit", tag_label="Exit Planning",
    pub_date="April 2, 2026", read_time="5 min read",
    slug="key-person-risk",
    body_html="""
<p>In 500+ transactions, the single most common valuation gap between what a founder expects and what buyers will pay is key person risk. It's invisible to the person causing it &mdash; because the founder is living inside the business &mdash; and obvious to every buyer who looks at it from the outside.</p>
<p>The question buyers are really asking when they dig into this isn't "is the founder involved?" It's "will the business still work after close?"</p>

<h2>How Buyers Score It</h2>
<p>PE firms and institutional buyers have a standard checklist for evaluating owner dependency. Here's what they look at:</p>
<ul>
  <li><strong>Customer relationships.</strong> Do customers call the owner directly? Do they know the owner by name? Would they stay if the owner left?</li>
  <li><strong>Supplier relationships.</strong> Are pricing, terms, or access dependent on the owner's personal relationships?</li>
  <li><strong>Operational knowledge.</strong> Is there documented process, or does the business run on the owner's knowledge of what to do in every situation?</li>
  <li><strong>Management depth.</strong> Is there a #2 who could run operations day-to-day? A CFO or controller who owns the financials?</li>
  <li><strong>Revenue attribution.</strong> Can the sales team generate new business, or does revenue depend on the owner's network and reputation?</li>
</ul>
<div class="callout"><strong>The buyer's logic:</strong> Every risk item above is a potential earn-out lever or price reduction. If the business is owner-dependent and the owner is leaving, the buyer is pricing in the cost of hiring people to replace everything the owner does &mdash; plus a risk premium for what they might miss.</div>

<h2>The Valuation Impact</h2>
<p>Key person risk is typically priced as a 0.5&ndash;1.5 turn discount to the multiple. On a $3M EBITDA business at a "clean" 7x = $21M, that risk costs $1.5M&ndash;$4.5M at the LOI stage. More often, it shows up in deal structure: higher earnouts, longer seller notes, lower upfront cash, and longer transition requirements for the owner.</p>
<table class="data-table">
  <thead><tr><th>Risk Level</th><th>Buyer Behavior</th><th>Typical Adjustment</th></tr></thead>
  <tbody>
    <tr><td>Low (strong #2, documented ops)</td><td>Full price, clean structure</td><td>None</td></tr>
    <tr><td>Moderate (some owner dependency)</td><td>Longer transition, modest earnout</td><td>&minus;0.5x, 6&ndash;12 month transition</td></tr>
    <tr><td>High (owner is the business)</td><td>Significant earnout, extended role requirement</td><td>&minus;1&ndash;2x, 2&ndash;3 year earnout</td></tr>
    <tr><td>Critical (no functioning team)</td><td>Pass, or management buyout structure only</td><td>Deal redesign required</td></tr>
  </tbody>
</table>

<h2>The Fix: A Practical Framework</h2>
<h3>Step 1: Identify Your #2</h3>
<p>The most important step is finding and empowering the person who can run the business day-to-day. This might be an existing operations manager you've been underutilizing, or it might require a hire. Budget 12&ndash;18 months for this person to develop visible authority before going to market.</p>

<h3>Step 2: Transfer Customer Relationships</h3>
<p>Systematically introduce your operations leader, account managers, or sales team to every key customer relationship you own personally. Start with your lowest-concentration customers and work up. The goal is that by go-to-market time, at least one other person has a strong relationship with each significant customer.</p>

<h3>Step 3: Document Everything</h3>
<p>Operations manuals, process documentation, and standard operating procedures aren't just for operations &mdash; they're evidence for buyers that institutional knowledge exists independent of any one person. They don't need to be elaborate; they need to be real.</p>

<h3>Step 4: Let Your Team Make Decisions Visibly</h3>
<p>In management presentations, buyers will specifically look for evidence of a functional team. Let your #2 lead parts of the presentation. Let your CFO explain the financial model. Demonstrate &mdash; don't just assert &mdash; that this is a team, not a one-person show.</p>
<div class="highlight"><p><strong>Bottom line:</strong> Reducing key person risk before going to market is the highest-ROI operational investment most founders can make. The work takes 12&ndash;18 months to do properly, which is why starting early matters. The cost is real but the payoff is multiples of what you put in.</p></div>
""")))

# 6. Earnouts
articles.append(('earnouts-explained.html', page(
    title="Earnouts Explained: When They Protect You and When They're a Trap",
    meta_desc="Earnouts appear in roughly 30% of lower middle market deals. Done right, they bridge valuation gaps. Done wrong, they're mechanisms that let buyers pay you less. Here's how to tell the difference.",
    tag_class="tag-deal", tag_label="Deal Structure",
    pub_date="March 28, 2026", read_time="10 min read",
    slug="earnouts-explained",
    body_html="""
<p>An earnout is a contractual provision where a portion of the purchase price is contingent on the business achieving specific performance targets post-close. They appear in roughly 30% of lower middle market deals and are among the most negotiated &mdash; and most misunderstood &mdash; elements of deal structure.</p>
<p>Earnouts can be legitimate tools for bridging valuation gaps. They can also be sophisticated mechanisms that allow buyers to pay you less than you agreed to. Here's how to know which one you're dealing with.</p>

<h2>When Earnouts Make Sense (For Both Sides)</h2>
<p>The legitimate use case for an earnout is a genuine valuation gap caused by future uncertainty. If your business had an exceptional year and you're projecting continued growth, but the buyer isn't confident projections will materialize, an earnout bridges that gap: you get paid if you're right.</p>
<p>Earnouts also make sense in acquisition structures where the seller will remain actively involved &mdash; typically 2&ndash;3 years &mdash; and the earnout is tied to performance metrics the seller can influence. In these cases, the earnout is less a valuation adjustment and more a performance incentive.</p>
<div class="callout"><strong>The key test:</strong> Can you control the outcome? If the earnout metric is tied to something within your operational control &mdash; revenue from your existing customer base, gross margin, your division's EBITDA &mdash; it may be workable. If it's tied to combined-company metrics, buyer integration decisions, or capital allocation choices the buyer controls, it's a trap.</div>

<h2>Earnout Structures That Favor Sellers</h2>
<ul>
  <li><strong>Revenue-based, not EBITDA-based.</strong> Revenue is harder for buyers to manipulate through cost allocation. EBITDA can be depressed post-close by integration costs, management fees, or shared service allocations that get charged to your business.</li>
  <li><strong>Short duration.</strong> 12&ndash;24 months is workable. Three years or more dramatically increases the chance that market conditions, integration decisions, or operational changes will make the targets unreachable for reasons outside your control.</li>
  <li><strong>Based on your division / book of business only.</strong> Combined-company metrics expose you to the buyer's other operations and integration choices.</li>
  <li><strong>Capped and clearly defined.</strong> Know exactly what the maximum payout is and exactly what triggers it. Ambiguity in earnout language always resolves in the buyer's favor during disputes.</li>
</ul>

<h2>Earnout Structures That Favor Buyers (Red Flags)</h2>
<ul>
  <li><strong>EBITDA-based with shared cost allocations.</strong> The buyer can charge management fees, IT overhead, shared services, and integration costs to your business, depressing EBITDA below the threshold.</li>
  <li><strong>Milestone-based on subjective criteria.</strong> "Successful integration," "customer retention at buyer's discretion," or "operational KPIs to be determined post-close" are blank checks for non-payment.</li>
  <li><strong>No non-interference provisions.</strong> If the buyer can change your pricing, redirect your sales team, switch your key customers to their platform, or terminate key employees &mdash; all of which would kill your earnout &mdash; and there's no contractual protection against it, you're exposed.</li>
  <li><strong>Long duration (3+ years).</strong> Over three years, the original conditions almost certainly won't hold. New management, market shifts, and integration changes will complicate attribution.</li>
</ul>

<h2>How to Negotiate Earnout Protections</h2>
<table class="data-table">
  <thead><tr><th>Risk</th><th>Protection to Request</th></tr></thead>
  <tbody>
    <tr><td>Buyer charges costs to your division</td><td>Cap on allocated overhead / management fees</td></tr>
    <tr><td>Buyer changes your go-to-market</td><td>Non-interference covenant for earnout period</td></tr>
    <tr><td>Buyer redirects key customers</td><td>Customer retention protection / approval rights</td></tr>
    <tr><td>Metric manipulation</td><td>Independent accountant determination of earnout</td></tr>
    <tr><td>Ambiguous targets</td><td>Specific, objectively measurable definitions</td></tr>
    <tr><td>Dispute resolution</td><td>Binding arbitration with CPA neutral, not litigation</td></tr>
  </tbody>
</table>

<h2>The Alternative: Push for More Cash at Close</h2>
<p>The best earnout protection is minimizing the earnout. In a competitive process, sellers have leverage to push buyers toward higher upfront cash and smaller contingent payments. Every dollar moved from the earnout column to the close column is a dollar you don't have to earn twice.</p>
<p>If a buyer insists on an earnout as a material part of the structure, it often signals either (a) genuine uncertainty about projections, in which case you should revisit your valuation basis, or (b) a negotiating strategy to reduce risk on their side by transferring it to yours.</p>
<div class="highlight"><p><strong>Bottom line:</strong> Earnouts are not inherently bad, but they require specific protections to be workable for sellers. If you can't get those protections in the LOI stage, assume the earnout won't pay &mdash; and price your acceptance decision accordingly.</p></div>
""")))

# ── Write all files ────────────────────────────────────────────────────────────
out_dir = os.path.dirname(os.path.abspath(__file__))
for fname, content in articles:
    path = os.path.join(out_dir, fname)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Written: {fname} ({len(content):,} chars)")

print(f"\nTotal: {len(articles)} articles")
