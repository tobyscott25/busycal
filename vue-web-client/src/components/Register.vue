<template>
    <form action="">
        <div>
            <label for="first_name">First Name</label>
            <input type="text" name="first_name" id="first_name">
        </div>
        <div>
            <label for="last_name">Last Name</label>
            <input type="text" name="last_name" id="last_name">
        </div>
        <div>
            <label for="email">Email Address</label>
            <input type="text" name="email" id="email" @input="setEmail">
            <p v-if="!isValidEmail">Not Valid</p>
        </div>
        <div>
            <label for="password">Password</label>
            <input type="text" name="password" id="password">
        </div>
        <button type="submit">Sign Up</button>        
    </form>
</template>

<script>
export default {
    data() {
        return {
            email: ""
        }
    },
    computed: {
        isValidEmail() {
            const re = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
            return re.test(this.email);
        }
    },
    methods: {
        setEmail(event){
            this.email = event.target.value;
        }
    }

}
</script>