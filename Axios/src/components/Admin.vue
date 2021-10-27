<template>
    <div class="container" style="margin-top: 20px">
        <div class="header">
            <h1 style="margin-left: 10px">Thông tin cá nhân </h1>
            <router-link 
            tag="button"
            style="margin-right: 10px" 
            class="fadeIn btn btn-success mr-2"
            to="/home">Quay về danh sách User</router-link>
        </div>
        <table style="margin-top: 20px" class="table" border="1" > 
            <tr>
            <th>Fullname</th>
            <td> {{admin.fullname}} </td>
            </tr>

            <tr>
            <th>Username</th>
            <td> {{admin.username}} </td>
            </tr>
            <tr>
                <th>Password</th>
                <!-- <td> {{adminl.password}} </td> -->
                <td> ******** </td>
            </tr>                  
            <tr>
            <th>Email</th>
            <td> {{admin.email}} </td>
            </tr>                   
            <tr>
            <th>Phonenumber</th>
            <td> {{admin.phonenumber}} </td>
            </tr> 
            <tr>
            <th>Position</th>
            <td> {{admin.position}} </td>  
            </tr>                            
        </table>
        <div class="Methods">
            <button class="btn btn-primary" @click="edit">Chỉnh sửa</button>
            <button class="btn btn-danger" @click="remove">Xóa</button> 
        </div>
      <div  v-if="flagChange" class="container">
        <br />
          <h1 >Chỉnh sửa thông tin</h1>
        <hr />
        <div class="row my-row">
          <div class="head">
            <h6 style="margin-right:12px; margin-bottom:6px">Fullname</h6>
            <!-- <h6 style="margin-bottom:6px" class="error" v-if="error.isFullname"> Please enter your fullname</h6> -->
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
            <h6 style="margin-right:12px; margin-bottom:6px">Password</h6>
            <!-- <h6 style="margin-bottom:6px" class="error" v-if="error.isPassword"> Please enter your password</h6> -->
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
            <!-- <h6 style="margin-bottom:6px" class="error" v-if="error.isEmail"> Please enter your email</h6> -->
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
            <!-- <h6 style="margin-bottom:6px" class="error" v-if="error.isPhonenumber"> Please enter your phonenumber</h6> -->
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
            <!-- <h6 style="margin-bottom:6px" class="error" v-if="error.isPosition"> Please enter your position</h6> -->
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
            <button class="btn btn-primary" @click="success_change">Change</button>
            <button class="btn btn-warning" @click="back">Quay lại</button>
        <br />
      </div>
      
    </div>
</template>
<script>
import axios from "axios"

export default {
  data () {
    return {
      admin: null,
      url: 'http://127.0.0.1:5000/',
      flagChange: false,
      fullname: null,
      password: null,
      email: null,
      phonenumber: null, 
      position: null,

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
    edit(){
        this.flagChange = true
        this.fullname = this.admin.fullname;
        this.password = this.admin.password;
        this.email = this.admin.email;
        this.phonenumber = this.admin.phonenumber;
        this.position = this.admin.position;
    },
    success_change(){
        this.admin.fullname = this.fullname
        this.admin.password = this.password
        this.admin.email = this.email
        this.admin.phonenumber = this.phonenumber
        this.admin.position = this.position
        axios
            .put(this.url +'admin/' + this.admin.username, this.admin)
            .then((response)=>{
                alert("Chỉnh sửa thành công")
                this.flagChange = false
            })
            .catch(error => alert(error))

    },
    back(){
      this.flagChange = false
    },
    remove(){
        axios
            .delete(this.url + "admin/" + sessionStorage.getItem('usernameAdmin'))
            .then((response) => {
                alert("Admin đã xóa")
                this.$router.push("/")
            })
            .catch(error => alert(error))
    },
  },
  mounted () {
    axios
      .get(this.url + 'admin/' + sessionStorage.getItem('usernameAdmin'))
      .then((response) => {
        this.admin = response.data
      })
      .catch(error => console.log(error))
  }
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
