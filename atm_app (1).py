import streamlit as st


class ATM:
    def __init__(self):
        self.pin = ""
        self.balance = 0

    def create_pin(self, pin, balance):
        self.pin = pin
        self.balance = balance

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            return True
        return False

    def check_balance(self, pin):
        return pin == self.pin

    def withdrawal(self, pin, amount):
        if pin != self.pin:
            return "wrong_pin"
        if amount > self.balance:
            return "low_balance"
        self.balance -= amount
        return "ok"


# Streamlit har click pe script dobara run karta hai,
# isliye ATM object ko session_state me save karte hain
if "atm" not in st.session_state:
    st.session_state.atm = ATM()

atm = st.session_state.atm

st.title("🏧 ATM Machine")

menu = st.sidebar.radio(
    "Menu",
    ["Create PIN", "Change PIN", "Check Balance", "Withdrawal"],
)

# ---------- 1) Create PIN ----------
if menu == "Create PIN":
    st.subheader("Create PIN")
    pin = st.text_input("Enter your PIN", type="password")
    balance = st.number_input("Enter balance", min_value=0, step=100)

    if st.button("Create PIN"):
        if pin == "":
            st.warning("PIN khali nahi ho sakta")
        else:
            atm.create_pin(pin, int(balance))
            st.success("Pin Created Successfully ✅")

# ---------- 2) Change PIN ----------
elif menu == "Change PIN":
    st.subheader("Change PIN")
    if atm.pin == "":
        st.warning("Pehle PIN create karo")
    else:
        old_pin = st.text_input("Enter old PIN", type="password")
        new_pin = st.text_input("Enter new PIN", type="password")

        if st.button("Change PIN"):
            if new_pin == "":
                st.warning("New PIN khali nahi ho sakta")
            elif atm.change_pin(old_pin, new_pin):
                st.success("PIN change ho gaya ✅")
            else:
                st.error("Not valid ❌ (old PIN galat hai)")

# ---------- 3) Check Balance ----------
elif menu == "Check Balance":
    st.subheader("Check Balance")
    if atm.pin == "":
        st.warning("Pehle PIN create karo")
    else:
        pin = st.text_input("Enter PIN", type="password")

        if st.button("Check Balance"):
            if atm.check_balance(pin):
                st.info(f"Your balance is: ₹{atm.balance}")
            else:
                st.error("Galat PIN ❌")

# ---------- 4) Withdrawal ----------
elif menu == "Withdrawal":
    st.subheader("Withdrawal")
    if atm.pin == "":
        st.warning("Pehle PIN create karo")
    else:
        pin = st.text_input("Enter PIN", type="password")
        amount = st.number_input("Enter amount", min_value=0, step=100)

        if st.button("Withdraw"):
            result = atm.withdrawal(pin, int(amount))
            if result == "ok":
                st.success(f"Withdrawal successful ✅ Balance: ₹{atm.balance}")
            elif result == "wrong_pin":
                st.error("Galat PIN ❌")
            else:
                st.error("Balance kam hai ❌")
