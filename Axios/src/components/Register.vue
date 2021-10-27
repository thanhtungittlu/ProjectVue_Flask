<template>
  <div id="app">
    <div  class="main">
      <div  class="container">
        <h1 >Thêm danh sách </h1>
        <hr />
        <div class="row my-row">
          <div v-if="!changeEdit" class="head">
            <h6 style="margin-right:12px; margin-bottom:6px">Fullname</h6>
            <h6 style="margin-bottom:6px" class="error" v-if="error.isFullname"> Please enter your fullname</h6>
          </div>
          <input
            v-if="!changeEdit"
            class="mb-3"
            style=""
            placeholder="Lê Thanh Tùng"
            @blur="blurFullname"
            @input="inputFullname"
            v-model="fullname"
            type="text"/>


          <div class="head">
            <h6 style="margin-right:12px; margin-bottom:6px">Username</h6>
            <h6 style="margin-bottom:6px" class="error" v-if="error.isUsername"> Please enter your username</h6>
          </div>
          <input
            class="mb-3"
            style=""
            placeholder="tunglt"
            @blur="blurUsername"
            @input="inputUsername"
            v-model="username"
            type="text"/>


          <div class="head">
            <h6 style="margin-right:12px; margin-bottom:6px">Password</h6>
            <h6 style="margin-bottom:6px" class="error" v-if="error.isPassword"> Please enter your password</h6>
          </div>
          <input
            class="mb-3"
            style=""
            placeholder="khongcopass"
            @blur="blurPassword"
            @input="inputPassword"
            v-model="password"
            type="password"/>


          <div class="head">
            <h6 style="margin-right:12px; margin-bottom:6px">Email</h6>
            <h6 style="margin-bottom:6px" class="error" v-if="error.isEmail"> Please enter your email</h6>
          </div>
          <input
            class="mb-3"
            style=""
            placeholder="99lethanhtung@gmail.com"
            @blur="blurEmail"
            @input="inputEmail"
            v-model="email"
            type="text"/>


          <div class="head">
            <h6 style="margin-right:12px; margin-bottom:6px">Phonenumber</h6>
            <h6 style="margin-bottom:6px" class="error" v-if="error.isPhonenumber"> Please enter your phonenumber</h6>
          </div>
          <input
            class="mb-3"
            style=""
            placeholder="0364959199"
            @blur="blurPhonenumber"
            @input="inputPhonenumber"
            v-model="phonenumber"
            type="text"/>


          <div class="head">
            <h6 style="margin-right:12px; margin-bottom:6px">Position</h6>
            <h6 style="margin-bottom:6px" class="error" v-if="error.isPosition"> Please enter your position</h6>
          </div>
          <input
            class="mb-3"
            style=""
            placeholder="Intern"
            @blur="blurPosition"
            @input="inputPosition"
            v-model="position"
            type="text"/>


        </div>
        <br />
        <button v-if="changeEdit" class="btn btn-primary" @click="success_change">Change</button>
        <button v-else class="btn btn-primary" @click="submit">Submit</button>
        <br />
        <br />
      </div>

      <div v-if="flagVerify" style="margin-top:20px;margin-left:40px">
          <p class="error">Bạn đã đăng ký thành công</p>
      </div>
    </div>

  </div>

</template>

<script>
import axios from "axios"

export default {
  data () {
    return {
      flagVerify : false,
      error: {
        isFullname: true,
        isUsername: true,
        isPassword: true,
        isEmail: true,
        isPhonenumber: true,
        isPosition: true,
      },

      admins: null,
      add_: {
        "fullname" : "",
        "username" :"",
        "password" :"",
        "email" :"",
        "phonenumber" :"",
        "position":"",
      },

      flagAdd: false,
      fullname: null,
      username: null,
      password: null,
      email: null,
      phonenumber: null, 
      position: null,
      url: 'http://127.0.0.1:5000/',
    }
  },
  methods: {
    blurFullname(e) {
      if (e.target.value.trim() == "") {
        this.error.isFullname = true;
      }
    },
    inputFullname() {
      this.error.isFullname = false;
    },
    blurUsername(e) {
      if (e.target.value.trim() == "") {
        this.error.isUsername = true;
      }
    },
    inputUsername() {
      this.error.isUsername = false;
    },

    blurPassword(e) {
      if (e.target.value.trim() == "") {
        this.error.isPassword = true;
      }
    },
    inputPassword() {
      this.error.isPassword = false;
    },

    blurEmail(e) {
      if (e.target.value.trim() == "") {
        this.error.isEmail = true;
      }
    },
    inputEmail() {
      this.error.isEmail = false;
    },

    blurPhonenumber(e) {
      if (e.target.value.trim() == "") {
        this.error.isPhonenumber = true;
      }
    },
    inputPhonenumber() {
      this.error.isPhonenumber = false;
    },

    blurPosition(e) {
      if (e.target.value.trim() == "") {
        this.error.isPosition = true;
      }
    },
    inputPosition() {
      this.error.isPosition = false;
    },
    checkInput(){
      if (this.error.isFullname == false && this.error.isUsername == false && this.error.isPassword == false && this.error.isEmail == false && this.error.isPhonenumber == false && this.error.isPosition == false ){
        return false
      }
      return true
    },
    submit(){

      if (this.checkInput() == false) {
        
        this.add_.fullname = this.fullname
        this.add_.username = this.username
        this.add_.password = this.password
        this.add_.email = this.email
        this.add_.phonenumber = this.phonenumber
        this.add_.position = this.position
        axios
            .post(this.url + "admin/" + this.fullname,this.add_)   
            .then((response) => {
                alert("Thêm admin thành công")
                this.$router.push("/")
            })
            .catch((error) =>{
                alert(error)
            })     
      }else{
        alert("Please enter your text")
      }
    },
  },
}

</script>

<style>

.error{
  color: red;
}
.head{
  display: flex;
}

/* BASIC */

.login>h2 {
  text-align: center;
  font-size: 16px;
  font-weight: 600;
  text-transform: uppercase;
  display:inline-block;
  margin: 40px 8px 10px 8px; 
  color: #cccccc;
}
.header {
  display: flex;
  flex-direction: row; 
  justify-content: space-between;
}



/* STRUCTURE */

.wrapper {
  display: flex;
  align-items: center;
  flex-direction: column; 
  justify-content: center;
  width: 100%;
  min-height: 100%;
  padding: 20px;
}

#formContent {
  -webkit-border-radius: 10px 10px 10px 10px;
  border-radius: 10px 10px 10px 10px;
  background: #fff;
  padding: 30px;
  width: 90%;
  max-width: 450px;
  position: relative;
  padding: 0px;
  -webkit-box-shadow: 0 30px 60px 0 rgba(0,0,0,0.3);
  box-shadow: 0 30px 60px 0 rgba(0,0,0,0.3);
  text-align: center;
}

#formFooter {
  background-color: #f6f6f6;
  border-top: 1px solid #dce8f1;
  padding: 25px;
  text-align: center;
  -webkit-border-radius: 0 0 10px 10px;
  border-radius: 0 0 10px 10px;
}



/* TABS */

.login>h2.inactive {
  color: #cccccc;
}

.login>h2.active {
  color: #0d0d0d;
  border-bottom: 2px solid #5fbae9;
}



/* FORM TYPOGRAPHY*/

input[type=button], input[type=submit], input[type=reset]  {
  background-color: #56baed;
  border: none;
  color: white;
  padding: 15px 80px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  text-transform: uppercase;
  font-size: 13px;
  -webkit-box-shadow: 0 10px 30px 0 rgba(95,186,233,0.4);
  box-shadow: 0 10px 30px 0 rgba(95,186,233,0.4);
  -webkit-border-radius: 5px 5px 5px 5px;
  border-radius: 5px 5px 5px 5px;
  margin: 5px 20px 40px 20px;
  -webkit-transition: all 0.3s ease-in-out;
  -moz-transition: all 0.3s ease-in-out;
  -ms-transition: all 0.3s ease-in-out;
  -o-transition: all 0.3s ease-in-out;
  transition: all 0.3s ease-in-out;
}

input[type=button]:hover, input[type=submit]:hover, input[type=reset]:hover  {
  background-color: #39ace7;
}

input[type=button]:active, input[type=submit]:active, input[type=reset]:active  {
  -moz-transform: scale(0.95);
  -webkit-transform: scale(0.95);
  -o-transform: scale(0.95);
  -ms-transform: scale(0.95);
  transform: scale(0.95);
}

input[type=text], input[type=password]{
  background-color: #f6f6f6;
  border: none;
  color: #0d0d0d;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 5px;
  width: 85%;
  border: 2px solid #f6f6f6;
  -webkit-transition: all 0.5s ease-in-out;
  -moz-transition: all 0.5s ease-in-out;
  -ms-transition: all 0.5s ease-in-out;
  -o-transition: all 0.5s ease-in-out;
  transition: all 0.5s ease-in-out;
  -webkit-border-radius: 5px 5px 5px 5px;
  border-radius: 5px 5px 5px 5px;
}

input[type=text]:focus, input[type=password]:focus{
  background-color: #fff;
  border-bottom: 2px solid #5fbae9;
}

input[type=text]:placeholder,input[type=password]:focus {
  color: #cccccc;
}



/* ANIMATIONS */

/* Simple CSS3 Fade-in-down Animation */
.fadeInDown {
  -webkit-animation-name: fadeInDown;
  animation-name: fadeInDown;
  -webkit-animation-duration: 1s;
  animation-duration: 1s;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
}

@-webkit-keyframes fadeInDown {
  0% {
    opacity: 0;
    -webkit-transform: translate3d(0, -100%, 0);
    transform: translate3d(0, -100%, 0);
  }
  100% {
    opacity: 1;
    -webkit-transform: none;
    transform: none;
  }
}

@keyframes fadeInDown {
  0% {
    opacity: 0;
    -webkit-transform: translate3d(0, -100%, 0);
    transform: translate3d(0, -100%, 0);
  }
  100% {
    opacity: 1;
    -webkit-transform: none;
    transform: none;
  }
}

/* Simple CSS3 Fade-in Animation */
@-webkit-keyframes fadeIn { from { opacity:0; } to { opacity:1; } }
@-moz-keyframes fadeIn { from { opacity:0; } to { opacity:1; } }
@keyframes fadeIn { from { opacity:0; } to { opacity:1; } }

.fadeIn {
  opacity:0;
  -webkit-animation:fadeIn ease-in 1;
  -moz-animation:fadeIn ease-in 1;
  animation:fadeIn ease-in 1;

  -webkit-animation-fill-mode:forwards;
  -moz-animation-fill-mode:forwards;
  animation-fill-mode:forwards;

  -webkit-animation-duration:1s;
  -moz-animation-duration:1s;
  animation-duration:1s;
}

.fadeIn.first {
  -webkit-animation-delay: 0.4s;
  -moz-animation-delay: 0.4s;
  animation-delay: 0.4s;
}

.fadeIn.second {
  -webkit-animation-delay: 0.6s;
  -moz-animation-delay: 0.6s;
  animation-delay: 0.6s;
}

.fadeIn.third {
  -webkit-animation-delay: 0.8s;
  -moz-animation-delay: 0.8s;
  animation-delay: 0.8s;
}

.fadeIn.fourth {
  -webkit-animation-delay: 1s;
  -moz-animation-delay: 1s;
  animation-delay: 1s;
}

/* Simple CSS3 Fade-in Animation */
.underlineHover:after {
  display: block;
  left: 0;
  bottom: -10px;
  width: 0;
  height: 2px;
  background-color: #56baed;
  content: "";
  transition: width 0.2s;
}

.underlineHover:hover {
  color: #0d0d0d;
}

.underlineHover:hover:after{
  width: 100%;
}



/* OTHERS */

*:focus {
    outline: none;
} 

#icon {
  width:60%;
}

</style>
