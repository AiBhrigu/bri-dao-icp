use candid::CandidType;
use serde::{Deserialize, Serialize};
use ic_cdk::query; // query макрос идёт из ic_cdk напрямую

#[derive(CandidType, Serialize, Deserialize)]
struct MyStruct {
    field: String,
}

#[query]
fn greet(name: String) -> String {
    format!("Hello, {}!", name)
}

ic_cdk::export_candid!();
