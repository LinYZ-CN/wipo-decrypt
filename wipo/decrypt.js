// 确保在引入 CryptoJS 库后才运行此代码
const CryptoJS = require('./crypto-js.min.js');

function decryptAES(encryptedText) {
    var decrypt = CryptoJS.AES.decrypt(encryptedText, "8?)i_~Nk7qv0IX;").toString(CryptoJS.enc.Utf8)
    return decrypt;
}
