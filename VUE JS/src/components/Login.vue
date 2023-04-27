<template>
    <div class="card">
        <form @submit.prevent="login">
            <br>
            <div class="form-group row">
                <label for="username" class="col-md-3 col-form-label">Username:</label>
                <div class="col-md-6">
                    <input type="text" id="username" class="form-control" v-model="username">
                </div>
            </div>
            <br>
            <div class="form-group row">
                <label for="password" class="col-md-3 col-form-label">Password:</label>
                <div class="col-md-6">
                    <input type="password" id="password" class="form-control" v-model="password">
                </div>
            </div>
            <br>
            <div class="form-group row">
                <div class="offset-md-3 col-md-6">
                    <button type="submit" class="btn btn-primary">Log in</button>
                </div>
            </div>
            <br>
        </form>
    </div>

</template>

<script>
    export default {
        data() {
            return {
                username: '',
                password: ''
            }
        },
        methods: {
            login() {
                // Agrega aquí la lógica de autenticación, por ejemplo, hacer una solicitud a un servidor API para verificar las credenciales del usuario
            }
        }
    }
</script>