<template>
    <form @submit.prevent="submitData">
        <div>
            <label for="first_name">First Name</label>
            <input type="text" name="first_name" id="first_name" v-model="firstName">
        </div>
        <div>
            <label for="last_name">Last Name</label>
            <input type="text" name="last_name" id="last_name" v-model="lastName">
        </div>
        <div>
            <label for="email">Email Address</label>
            <input type="text" name="email" id="email" v-model="email">
            <p v-if="!isValidEmail">Not Valid</p>
        </div>
        <div>
            <label for="password">Password</label>
            <input type="text" name="password" id="password" v-model="password">
        </div>
        <button type="submit">Sign Up</button>        
    </form>
</template>

<script>
export default {
    data() {
        return {
            email: "",
            firstName: "",
            lastName: "",
            password: ""
        }
    },
    methods: {
        submitData() {
            //Submit data
        }
    },
    computed: {
        isValidEmail() {
            const re = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
            return re.test(this.email);
        }
    }
}
</script>