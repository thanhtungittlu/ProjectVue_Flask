<template>
  <div id="app">
    <div v-if="AuthLogin" class="container">
      <div  class="header" style="margin-top: 10px">
        <h1 style="margin-left: 10px">Danh sách {{btn}} </h1>
        <div>
              <router-link 
                tag="button"
                style="margin-right: 10px" 
                class="fadeIn btn btn-success mr-2"
                to="/admin">Xem thông tin cá nhân</router-link>
                
            <button 
                style="margin-right: 10px" 
                class="fadeIn btn btn-danger mr-2"
                @click="logOut"
               >Logout</button>            

        </div>
      </div>
      <hr>
      <!-- <button @click="get">Làm mới danh sách.</button> -->
      <div  v-for="user in users" v-bind:key="user">
        <table class="table">
              <thead>
                <tr>
                  <th>STT</th>
                  <th>Fullname</th>
                  <th>Username</th>
                  <th>Password</th>
                  <th>Email</th>
                  <th>Phonenumber</th>
                  <th>Position</th>
                  <th>Verify</th>
                  <th>Methods</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(userl,index) in user" v-bind:key="index">
                    <td>{{index + 1}}</td>
                    <td> {{userl.fullname}} </td>
                    <td> {{userl.username}} </td>
                    <!-- <td> {{userl.password}} </td> -->
                    <td> ******** </td>
                    <td> {{userl.email}} </td>
                    <td> {{userl.phonenumber}} </td>
                    <td> {{userl.position}} </td>
                    <td><p  style="cursor:pointer" @click="verify(userl)">{{userl.verify}}</p></td>
                    <td> 
                      <button class="btn btn-primary" @click="edit(userl)">Chỉnh sửa</button>  
                      <button class="btn btn-danger" @click="remove(userl)">Xóa</button>
                    </td>
                </tr> 
              </tbody>
          </table>
      </div>  

      <button v-if ="!flagVerify" @click="getNew" class="btn btn-success" >Làm mới danh sách</button>
      <button v-if ="!flagVerify" @click="addNewItem" class="btn btn-warning">Thêm mới danh sách</button>

      <div  v-if="flagAdd" class="container">
        <br />
          <h1 v-if="changeEdit" >Chỉnh sửa </h1>
          <h1 v-else>Thêm danh sách </h1>
        <hr />
        <div class="row my-row">
          
          <div v-if="!changeEdit" class="head">
            <h6 style="margin-right:12px; margin-bottom:6px">Fullname</h6>
            <h6 style="margin-bottom:6h6x" class="error" >(*)</h6>
          </div>
          <input
            v-if="!changeEdit"
            class="mb-3"
            style=""
            placeholder="Lê Thanh Tùng"
            v-model="fullname"
            type="text"/>


          <div v-if="!changeEdit" class="head">
            <h6 style="margin-right:12px; margin-bottom:6px">Username</h6>
            <h6 style="margin-bottom:6px" class="error" > (*)</h6>
          </div>
          <input
            v-if="!changeEdit"
            class="mb-3"
            style=""
            placeholder="tunglt"
            v-model="username"
            type="text"/>


          <div class="head">
            <h6 style="margin-right:12px; margin-bottom:6px">Password</h6>
            <h6 style="margin-bottom:6px" class="error" > (*)</h6>
          </div>
          <input
            class="mb-3"
            style=""
            placeholder="matkhau@994"
            v-model="password"
            type="password"/>

          <div class="head">
            <h6 style="margin-right:12px; margin-bottom:6px">Email</h6>
            <h6 style="margin-bottom:6px" class="error" > (*)</h6>
          </div>
          <input
            class="mb-3"
            style=""
            placeholder="99lethanhtung@gmail.com"
            v-model="email"
            type="text"/>

          <div class="head">
            <h6 style="margin-right:12px; margin-bottom:6px">Phonenumber</h6>
            <h6 style="margin-bottom:6px" class="error" > (*)</h6>
          </div>
          <input
            class="mb-3"
            style=""
            placeholder="0364959199"
            v-model="phonenumber"
            type="text"/>


          <div class="head">
            <h6 style="margin-right:12px; margin-bottom:6px">Position</h6>
            <h6 style="margin-bottom:6px" class="error" > (*)</h6>
          </div>
          <input
            class="mb-3"
            style=""
            placeholder="Intern"
            v-model="position"
            type="text"/>


        </div>
        <br />
        <button v-if="changeEdit" class="btn btn-primary" @click="success_change">Change</button>
        <button v-else class="btn btn-primary" @click="submit">Submit</button>
        <br />
        <br />
      </div>

      <div v-if="flagVerify" style="margin-top:100px;margin-left:40%">
          <h3>Bạn đã đăng ký thành công</h3>
          <button  @click="verifyAdd" class="btn btn-info" >Ấn vào đây để xác thực Email</button>
          <button  @click="back" class="btn btn-danger" >Trở về</button>
      </div>
    </div>

  </div>

</template>

<script>
import axios from "axios"

export default {
  data () {
    return {
      AuthStr: null,
      AuthLogin : false,
      flagVerify : false,
      admins: null,
      users: null,
      btn: "User",
      flag: false,
      changeEdit: false,
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
      url: 'http://192.168.101.122:5000/',
    }
  },
  methods: {
    logOut(){
      this.$router.push("/")
      sessionStorage.setItem('loginVerify', false)
      this.AuthLogin = false
    },
    addNewItem(){
      this.flagVerify = false
      this.flagAdd = true
      this.changeEdit= false
      this.resetChange()
    },
    back(){
      this.resetChange()
      this.flagAdd = false    
      this.flagVerify = false
    },
    verify(user){
      if (user.verify == true) {
        alert("Tài khoản đã được xác nhận")
      }else{
        axios
            .get(this.url + 'email/' + user.uuid)
            .then((response) => {
                alert("Vui lòng vào Email của bạn để xác nhận. ")
                this.resetChange()
                this.flagAdd = false    
                this.flagVerify = false
            })
            .catch(error => console.log(error))         
      }
    },
    verifyAdd(){
        axios
            .get(this.url + 'email/' + this.users.users[this.users.users.length-1].uuid)
            .then((response) => {
                alert("Vui lòng vào Email của bạn để xác nhận. Nếu không nhận được Email vui lòng click vào trường Verify để xác nhận lại")
                this.resetChange()
                this.flagAdd = false    
                this.flagVerify = false
            })
            .catch(error => console.log(error)) 
    },
    removeAscent (str) {
      if (str === null || str === undefined) return str;
        str = str.toLowerCase();
        str = str.replace(/à|á|ạ|ả|ã|â|ầ|ấ|ậ|ẩ|ẫ|ă|ằ|ắ|ặ|ẳ|ẵ/g, "a");
        str = str.replace(/è|é|ẹ|ẻ|ẽ|ê|ề|ế|ệ|ể|ễ/g, "e");
        str = str.replace(/ì|í|ị|ỉ|ĩ/g, "i");
        str = str.replace(/ò|ó|ọ|ỏ|õ|ô|ồ|ố|ộ|ổ|ỗ|ơ|ờ|ớ|ợ|ở|ỡ/g, "o");
        str = str.replace(/ù|ú|ụ|ủ|ũ|ư|ừ|ứ|ự|ử|ữ/g, "u");
        str = str.replace(/ỳ|ý|ỵ|ỷ|ỹ/g, "y");
        str = str.replace(/đ/g, "d");
        return str;
    },    
    checkErrorFullname(){
      var regexName = /^[a-zA-Z ]{2,}$/g;
      if(!regexName.test(this.removeAscent(this.fullname))){
        return true // Có lỗi 
      }else{
        return false // Không có lỗi
      }
    },
    checkErrorUsername(){
      var regexName = /^[a-zA-Z0-9_]{4,}[a-zA-Z]+[0-9]*$/ // a-z, gồm chữ số, có dấu gạch dưới, nhưng không được để cuối cùng, ít nhât 5 ký tự
      if (!regexName.test(this.username)){
        return true
      }else{
        return false
      }
    },
    checkErrorPassword(){
      var regexName = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/ // Ít nhất 6 ký tự, có thể có ký tự đặc biệt
      if (!regexName.test(this.password)){
        return true
      }else{
        return false
      }
    },
    checkErrorEmail(){
      var regexName = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/ // Ít nhất 6 ký tự, có thể có ký tự đặc biệt
      if (!regexName.test(this.email)){
        return true
      }else{
        return false
      }
    },
    checkErrorPhonenumber(){
      var regexName = /^[0-9]{8,11}$/;
      if(!regexName.test(this.removeAscent(this.phonenumber))){
        return true // Có lỗi 
      }else{
        return false // Không có lỗi
      }
    },
    checkErrorPosition(){
      var regexName = /^[a-zA-Z ]{2,}$/g;
      if(!regexName.test(this.removeAscent(this.position))){
        return true // Có lỗi 
      }else{
        return false // Không có lỗi
      }
    },
    checkErrorInput(){
      if (this.checkErrorFullname() == false && 
          this.checkErrorUsername() == false && 
          this.checkErrorPassword() == false && 
          this.checkErrorEmail() == false &&  
          this.checkErrorPhonenumber() == false && 
          this.checkErrorPosition() == false ){
        return false // tất cả không có lỗi thì trả về không lỗi
      }
      return true
    },
    getNew(){
        this.btn = "User"
        axios
          .get(this.url + "users",{ 'headers': { 'Authorization': this.AuthStr }})
          .then((response) => {
            this.users = response.data
            this.resetChange()
            this.flagAdd = false
          })
          .catch(error => alert("getall",error))
    },
    resetChange(){
      this.fullname = ""
      this.username = ""
      this.password = ""
      this.email = ""
      this.phonenumber = "" 
      this.position = ""
    },

    submit(){
      if (this.checkErrorInput() == false) {
        this.add_.fullname = this.fullname
        this.add_.username = this.username
        this.add_.password = this.password
        this.add_.email = this.email
        this.add_.phonenumber = this.phonenumber
        this.add_.position = this.position
    
        axios
          .post(this.url + "user/" + this.username,this.add_,{ 'headers': { 'Authorization': this.AuthStr } })
          .then((response) => {
            axios
              .get(this.url + "users",{ 'headers': { 'Authorization': this.AuthStr }})
              .then((response) => {
                this.users = response.data
                sessionStorage.setItem('uuid', this.users.users[this.users.users.length-1].uuid)
              })
              .catch(error => alert("getall",error))
            this.flagVerify = true   
            this.flagAdd = false
          })
          .catch(error => {
            alert("Username hoặc email đã tồn tại. ")
          })
      }else{
        alert("Bạn hãy nhập theo yêu cầu.")
      }
    },
    remove(dataRemove){ 
      axios
        .delete(this.url + "user/" + dataRemove.username,{ 'headers': { 'Authorization': this.AuthStr }})
        .then((response) => {
          axios
            .get(this.url + "users",{ 'headers': { 'Authorization': this.AuthStr }})
            .then((response) => {
              this.users = response.data
            })
        }) 
        .catch(error => alert(error))
    },
    edit(dataEdit) {

      this.flagAdd = true
      this.changeEdit = true
      this.fullname = dataEdit.fullname
      this.username = dataEdit.username
      this.password = dataEdit.password
      this.email = dataEdit.email
      this.phonenumber = dataEdit.phonenumber 
      this.position = dataEdit.position     

    },
    success_change(){
    
      if (this.checkErrorInput() == false) {
        this.add_.fullname = this.fullname
        this.add_.username = this.username
        this.add_.password = this.password
        this.add_.email = this.email
        this.add_.phonenumber = this.phonenumber
        this.add_.position = this.position     
        axios
            .put(this.url + "user/" + this.username,this.add_,{ 'headers': { 'Authorization': this.AuthStr }})
            .then((response) => {
              axios
                .get(this.url + "users",{ 'headers': { 'Authorization': this.AuthStr }})
                .then((response) => {
                  this.users = response.data
                })
            }) 
            .catch(error => alert(error))
        
        this.resetChange()
        this.flagAdd = false 
      }else{
        alert("Please enter your text")
      }
                  
    },
  },
  mounted () {
    if (sessionStorage.getItem('loginVerify') == "true") {
      this.AuthLogin = true;
    }else{
      this.AuthLogin = false;
    }
    console.log(typeof this.AuthLogin)
    this.AuthStr = 'JWT ' + sessionStorage.getItem('token');
    axios
      .get(this.url + 'admins')
      .then((response) => {
        this.admins = response.data
      })
      .catch(error => console.log(error))
    axios
      .get(this.url + 'users', { 'headers': { 'Authorization': this.AuthStr } })
      .then((response) => {
        this.users = response.data
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
