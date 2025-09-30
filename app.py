import streamlit as st
import pandas as pd
import plotly.express as px
from wallet_utils import RPCS, WALLETS, get_chain_balances, get_token_balances

st.set_page_config(page_title="Multi-Wallet Web3 Portfolio", layout="wide")

st.title("📊 Multi-Wallet Portfolio Tracker")
st.caption("Track balances across multiple wallets & chains")

all_data = []
for chain, rpc in RPCS.items():
    wallets = WALLETS.get(chain, [])
    if not wallets: 
        continue
    balances = get_chain_balances(chain, rpc, wallets)
    for b in balances:
        all_data.append({"Chain": chain, "Wallet": b["Wallet"], "Balance (ETH)": b["Balance"]})

df = pd.DataFrame(all_data)

# Tabel breakdown
st.subheader("💰 Balances per Wallet")
st.dataframe(df)

# Total per chain
chain_summary = df.groupby("Chain")["Balance (ETH)"].sum().reset_index()
st.subheader("📈 Total per Chain")
st.table(chain_summary)

# Grafik
fig = px.bar(chain_summary, x="Chain", y="Balance (ETH)", title="Total Balance per Chain")
st.plotly_chart(fig, use_container_width=True)

# Token breakdown (ambil dari wallet pertama Ethereum)
st.subheader("🪙 Token Portfolio (via Covalent API)")
tokens = get_token_balances(df.iloc[0]["Wallet"]) if not df.empty else []
if tokens:
    token_df = pd.DataFrame([{
        "Token": t["contract_ticker_symbol"],
        "Balance": int(t["balance"]) / (10 ** t["contract_decimals"]),
        "Value ($)": t["quote"]
    } for t in tokens])

    st.dataframe(token_df)
    pie = px.pie(token_df, names="Token", values="Value ($)", title="Token Distribution ($)")
    st.plotly_chart(pie, use_container_width=True)
else:
    st.info("No token data found (Covalent API needed).")
