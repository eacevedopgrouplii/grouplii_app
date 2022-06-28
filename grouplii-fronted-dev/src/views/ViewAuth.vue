<template>
    <div>
    <b-card no-body class="overflow-hidden" style="max-width: 540px;">
        <b-row no-gutters>
        <b-col md="6">
            <b-card-img src="@/assets/Logo_grouplii.jpg" alt="Image" class="rounded-0"></b-card-img>
        </b-col>
        <b-col md="6">
            <b-card-body title="Inicializando conexión con Dropbox">
            <b-card-text>
                Creando el acceso para almacenar imagenes Dropbox.
            </b-card-text>
            </b-card-body>  
        </b-col>
        </b-row>
    </b-card>
</div>
</template>

<script>
    export default {
        data() {
            return {                
                code: this.$route.query.code
            }
        },
        
            created: function () {

            const config = {
                    clientId: 'ybt65cfr2ldy2qo',
                    clientSecret: 'xot0v27neki5jwh',
                };

                var Dropbox = require('dropbox').Dropbox;
                var dbx = new Dropbox(config)

                dbx.auth.getAccessTokenFromCode("https://container-grouplii-frontend-uymd3d36pa-uc.a.run.app/auth", this.code)
                .then((response) => {                    
                    console.log(response.result.access_token);
                    console.log(`Token Result:${JSON.stringify(response.result.access_token)}`);
                    //this.$router.go(-3)
                    localStorage.setItem('token_drop',JSON.stringify(response.result.access_token));
                    window.close()
                    //this.$router.push({ path: '/home/new_inventory', params: { test: 'hello there' }});




                    //this.$router.push({ path: '/home/new_inventory' })
                    
                    dbx.usersGetCurrentAccount()
                        .then((response) => {
                        console.log('response', response);
                        })
                        .catch((error) => {
                        console.error(error);
                        });
                    })
                .catch((error) => {
                    console.error(error);
                    });
        }
    }
</script>

