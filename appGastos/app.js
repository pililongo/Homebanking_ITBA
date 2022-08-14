window.onunload = function () {
  localStorage.removeItem('expenses');
  localStorage.removeItem('friends');
}

function reset(e){
  localStorage.clear('expenses');
  document.location.reload(true);
}

function firstCap(name){
  name = name.charAt(0).toUpperCase() + name.slice(1);
  return(name);
}

document.getElementById('formExpense').addEventListener('submit', saveExpense);
let id = 0;

function saveExpense(e){
  let name = firstCap(document.getElementById('name').value);
  let amount = document.getElementById('amount').value;
  let description = document.getElementById('description').value;
  let sum = 0;
  id++;
  
  // let expenses = JSON.parse(localStorage.getItem('expenses'));
  
  let expense = {
    name,
    amount,
    description,
    id
  };

  let friend = {
    name,
    total: []
  }

  if(!localStorage.getItem('expenses')) {
    let expenses = [];
    expenses.push(expense);
    localStorage.setItem('expenses', JSON.stringify(expenses));
    
      let friends = JSON.parse(localStorage.getItem('friends'));
      friends.forEach((f) => f.name === name && f.total.push(parseInt(amount)))
      // friends.total.push(parseInt(friends.total[0]) += parseInt(amount));
      localStorage.setItem('friends', JSON.stringify(friends));

  } else {
    let expenses = JSON.parse(localStorage.getItem('expenses'));
    expenses.push(expense);
    localStorage.setItem('expenses', JSON.stringify(expenses));

    let friends = JSON.parse(localStorage.getItem('friends'));
    // sum = parseInt(amount) + f
    friends.forEach((f) => f.name === name && (f.total[0] += (parseInt(amount))));

    localStorage.setItem('friends', JSON.stringify(friends));
  }

  getExpense();
  document.getElementById('formExpense').reset();
  e.preventDefault();
}

function deleteExpense(id){
  let expenses = JSON.parse(localStorage.getItem('expenses'));
  let newExpensesArray = expenses.filter((e) => id !== e.id);
  let friends = JSON.parse(localStorage.getItem('friends'));
  let indexofExp = expenses.findIndex((i) => id === i.id);
  
  for(let i = 0; i < friends.length; i++){
    if (friends[i].name === expenses[indexofExp].name){
      friends[i].total[0] -= expenses[indexofExp].amount
    }
  }
  
  localStorage.setItem('expenses', JSON.stringify(newExpensesArray));
  localStorage.setItem('friends', JSON.stringify(friends));
  getExpense();
}


function getExpense(){
  let expenses = JSON.parse(localStorage.getItem('expenses'));
  let friends = JSON.parse(localStorage.getItem('friends'));
  let expensesView = document.getElementById('expenses');
  expensesView.innerHTML = '';
  let sum = 0;
  let div = 1;
  let each = 0;

  if(expenses.length === 0){
    total.innerHTML = 'Total: $0';
    perPerson.innerHTML = '0';
  }

  if(expenses){
    for(let i = 0; i < expenses.length; i++) {
    let name = expenses[i].name;
    let amount = expenses[i].amount;
    let description = expenses[i].description;
    let id = expenses[i].id;
    
    if(document.getElementById(name)){
      let newExpenseData = document.createElement('p');
      let newExpense = document.createTextNode(`$${amount}`);
      newExpenseData.appendChild(newExpense);
      document.getElementById(`desgloseExpenses${name}`).appendChild(newExpenseData);

      let newDescriptionData = document.createElement('p');
      let newDescription = document.createTextNode(`${description}`);
      newDescriptionData.appendChild(newDescription);
      document.getElementById(`desgloseDescrptions${name}`).appendChild(newDescriptionData);

      let newButton = document.createElement('button');
      let newDeleteButton = document.createTextNode('X');
      newButton.appendChild(newDeleteButton);
      newButton.setAttribute('class', "btn btn-sm float-right");
      newButton.setAttribute("onclick", `deleteExpense(${id})`);
      document.getElementById(`deleteButtons${name}`).appendChild(newButton);

    } else{
      expensesView.innerHTML += `<div class="card mb-3" id="${name}">
        <div class="card-body" id='cardBody'>
          <div>
            <p>${name}<p> 
          </div>
          <div id='desgloseExpenses${name}'>
            <p id='firstExpense'>$${amount}</p>
          </div>
          <div id='desgloseDescrptions${name}'>
            <p>${description}</p>
          </div>
          <div id='deleteButtons${name}' class='deleteButtons'>
            <button class="btn btn-sm float-right" id="reset" onclick="deleteExpense(${id})">X</button>
          </div>
        </div>
      </div>`;
    }


    sum += parseInt(amount);
    total.innerHTML = 'Total: $' + sum;

    div = Math.round(parseInt(sum) / friends.length);
    perPerson.innerHTML = div;

    }
  }
}

function addFriend(){
  let group = document.getElementById("name");
  let option = document.createElement("OPTION");
  let friend = firstCap(document.getElementById("friend").value);
  let members = document.getElementById("members");
  let expenses = JSON.parse(localStorage.getItem('expenses'));

  if(friend){
    option.innerHTML = friend;
    group.options.add(option);
    document.getElementById("friend").value = '';
    members.innerHTML += `<div class="card mb-3" ${friend}>
        <div class="card-body">
          <p>${friend} - $0
          <a href="#" onclick="deleteFriend('${friend}')" class="btn btn-sm float-right">X</a>
          </p>
        </div>
      </div>`;
    document.getElementById('formExpense').reset();
  }

   let expense = {
    name: friend,
    total: []
  };

  if(!localStorage.getItem('friends')) {
    let friends = [];
    friends.push(expense);
    localStorage.setItem('friends', JSON.stringify(friends));
  } else {
    let friends = JSON.parse(localStorage.getItem('friends'));
    friends.push(expense);
    localStorage.setItem('friends', JSON.stringify(friends));
  }

  division()
}

function division(){
  // let expenses = JSON.parse(localStorage.getItem('expenses')).concat(JSON.parse(localStorage.getItem('friends')))
  // let each = [];
  let count = document.getElementById("members").childElementCount;
  members.innerHTML = '';
  // let sum = 0;
  let friends = JSON.parse(localStorage.getItem('friends'));


  if(localStorage.getItem('friends').length > 0){
     for(let i = 0; i < friends.length; i++){
        let sumTotal = friends[i].total.reduce(function(sum, value) {
          return parseInt(sum) + parseInt(value);
        }, 0);

    friends[i].total = [];
    localStorage.setItem('friends', JSON.stringify(friends));
    friends[i].total.push(sumTotal);
    localStorage.setItem('friends', JSON.stringify(friends));
    }
  } 

  

  // for(let i = 0; i < each.length; i++) {
}

function showDivision(){
  members.innerHTML = '';
  let friends = JSON.parse(localStorage.getItem('friends'));

    friends.forEach((f) => 
      members.innerHTML += `<div class="card mb-3" id="${f.name}">
        <div class="card-body">
          <p>${f.name} - $ ${f.total[0] - parseInt(perPerson.innerHTML)}</p>
          </div>
        </div>`
    )
}
