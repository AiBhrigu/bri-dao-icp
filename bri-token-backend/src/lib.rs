use std::cell::RefCell;
use std::collections::HashMap;
use ic_cdk::export::Principal;

thread_local! {
    static BALANCES: RefCell<HashMap<Principal, u64>> = RefCell::new(HashMap::new());
}

#[ic_cdk::update]
fn icrc1_transfer(from: Principal, to: Principal, amount: u64) -> String {
    let caller = ic_cdk::caller();
    assert_eq!(caller, from, "Only owner can transfer!");

    BALANCES.with(|b| {
        let mut balances = b.borrow_mut();
        let from_balance = *balances.get(&from).unwrap_or(&0);
        assert!(from_balance >= amount, "Insufficient funds");

        balances.insert(from, from_balance - amount);
        let to_balance = *balances.get(&to).unwrap_or(&0);
        balances.insert(to, to_balance + amount);
    });

    format!("Transferred {} tokens from {:?} to {:?}", amount, from, to)
}