const get_data_json = async (url)=>{
    const headers = {
        'x-requested-with':'XMLHttpRequest',
        // 'access_token':access_token
    }
    let res = await axios.get(url,{headers:headers})
    res = res['data']
    return res
}

// const post_data_json_fb = async (url,access_token,dataPost)=>{
//     // console.log('dataPost',dataPost)
//     const headers = {
//         'x-requested-with':'XMLHttpRequest',
//         'access_token':access_token
//     }
//     let res =await axios.post(url,dataPost ,{headers:headers});
//     res = res['data']

//     // // !!! ADD LOGGING
//     // let logDataPost = [
//     //     url,
//     //     access_token,
//     //     dataPost
//     // ]
//     // logListDataPost = [...logListDataPost,logDataPost]

//     return res
// }
