<template>
<div >
  <nav class="navbar navbar-dark navbar-expand-sm" style="background: rgb(8, 40, 160)">
  <a class="navbar-brand" href="/home/admin">
    <img src="@/assets/Logo_grouplii.jpg"  width="150" height="50" alt="logo">
  </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbar-list-4" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  

  <div class="collapse navbar-collapse" id="navbar-list-4">
    <ul class="navbar-nav">
        <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <img src="https://cdn2.iconfinder.com/data/icons/facebook-51/32/FACEBOOK_LINE-01-512.png" width="40" height="40" class="rounded-circle">
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
          <a class="dropdown-item" href="#">Dashboard</a>
          <a class="dropdown-item" href="#">Edit Profile</a>
          <a class="dropdown-item" href="#">Log Out</a>
        </div>
      </li>   
    </ul>
  </div>
</nav>
</div>
</template>

<script>
export default {
  name: 'CNavbarP'
}
</script>

<style scoped>

.navbar{
    padding: 0%;
}

</style>