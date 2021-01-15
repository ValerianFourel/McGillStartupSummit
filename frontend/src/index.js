import React from "react";
import ReactDOM, { render } from "react-dom";
import { motion } from 'framer-motion';
// import Fade from 'react-reveal/Fade';
import style from './css.style.css';


const elements = {

  statement: document.getElementById('statement'),
  goToRegister: document.getElementById('goToRegister'),
//  jumbotron3: document.getElementById('jumbotron3'),
  statementHold: document.getElementById('statementHold'),
  registrationBox: document.getElementById('registration_box2'),
  jumbotron2: document.getElementById('jumbotron2'),
  viewTeam: document.getElementById('viewTeam'),
  Team: document.getElementById('Team'),
  changeProfil: document.getElementById('changeProfil'),
  ProfilChange: document.getElementById('ProfilChange'),
  form1: document.getElementById('form1'),
  editInfoUnId: document.getElementById('editInfoUnId'),
  memberShow: document.getElementById('memberShow'),
  memberHeaderShow: document.getElementById('memberHeaderShow'),
  form4Password: document.getElementById('form4Password'),











}


document.addEventListener("load", e=>{


  elements.form1.reset();



});




function clearBox(element) {
  var div = element;

  while(div.firstChild) {
      div.removeChild(div.firstChild);
          }
      }







const Statement = () => {

  return(<div className={style.statement}>
    <h4>
    Welcome to the McGill Startup Summit.
      <br></br>
             Our mission statement
            is to broaden and deepen the knowledge and
             experience of undergraduate students in the
             exciting and dynamic world of startup
             across North America.
             <br></br><br></br>
             Thank you for your interest and take care of yourself.
                 <br></br><br></br>
           </h4>
             <button className={style.goToRegister} onClick={renderRegistrationBox}>
               <h4>Continue to registration</h4>
               </button>
           </div>);


}







  if(elements.statementHold) ReactDOM.render(<Statement />, elements.statementHold);


  function renderRegistrationBox(){

    elements.registrationBox.style.display = "flex";


  }




document.addEventListener("load", e=>{

    if(elements.memberHeaderShow) {


    elements.Team.style.display = "block";

  }






  });





if(elements.viewTeam) {
  elements.Team.style.display = "none";
  if(elements.memberShow && elements.memberHeaderShow) {
    elements.Team.style.display = "block";


}


elements.viewTeam.addEventListener('click', e=>{

if(elements.form4Password) elements.form4Password.style.display = "none";



if(elements.memberShow && elements.memberHeaderShow) {



  if (elements.memberShow.style.display === "none" && elements.memberHeaderShow.style.display === "none") {
    elements.Team.style.display = "block";
    elements.memberShow.style.display = "block";
    elements.memberHeaderShow.style.display = "block";


  } else {
    elements.Team.style.display = "none";
    elements.memberShow.style.display = "none";
    elements.memberHeaderShow.style.display = "none";


  }



}else {

  if (elements.Team.style.display === "none") {

    elements.Team.style.display = "block";

  } else {

    elements.Team.style.display = "none";

  }

}


});

}




const EditInfoNull = () => {

  return(<div className={style.statement}>
    <h4>
    Welcome to the McGill Startup Summit Website.
      <br></br>
             It would seem you have arrived on this page by error.
             <br></br>
             Please login or create an account to Edit your Personal Information.
             <br></br>
             Thank you for your interest and take care of yourself.
                 <br></br><br></br>
           </h4>

           </div>);


}

if(elements.editInfoUnId) {

  ReactDOM.render(<EditInfoNull />, elements.editInfoUnId);



}
