use std::cell::RefCell;

#[derive(Clone)]
pub struct Proposal {
    id: u64,
    title: String,
    description: String,
    votes_yes: u64,
    votes_no: u64,
    executed: bool,
}

thread_local! {
    static PROPOSALS: RefCell<Vec<Proposal>> = RefCell::new(Vec::new());
}

#[ic_cdk::update]
fn create_proposal(title: String, description: String) -> u64 {
    PROPOSALS.with(|p| {
        let mut proposals = p.borrow_mut();
        let id = proposals.len() as u64 + 1;
        proposals.push(Proposal {
            id,
            title,
            description,
            votes_yes: 0,
            votes_no: 0,
            executed: false,
        });
        id
    })
}