<script>
    let ping_count = 0
    async function ping () {
        const res = await fetch('http://127.0.0.1:5000/ping', {
            method: "GET",
            credentials: 'include',
            headers: {
                "Content-Type": "application/json"
            },
        })
        
        const result = await res.json()
        if (result.message == "pong"){
            ping_count ++
        }
        
    }
</script>

number of pings = {ping_count} <br>
<input type="button" value="ping me!" on:click={ping}>