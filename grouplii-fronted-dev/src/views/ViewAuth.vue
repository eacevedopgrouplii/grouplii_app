<template>
    <div>
        <h1>Hi!
            <small class="text-muted">I am page 1!</small>
        </h1>
        <p>I have a dynamic id value of {{code}}</p>        
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

                dbx.auth.getAccessTokenFromCode("http://https://container-grouplii-frontend-uymd3d36pa-uc.a.run.app/auth", this.code)
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

