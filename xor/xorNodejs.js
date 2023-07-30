const CryptoXor = {
    encrypt: (plainString, key) => {
        let cypher = '';

        for (let i = 0; i < plainString.length; i++) {

            // Find ascii code from key to be "xor"
            const keyPointer = i % key.length;

            // Convert char to int ASCII and "xor crypt" with int ASCII
            const dec = parseInt((plainString[i]).charCodeAt(0) ^ (key[keyPointer]).charCodeAt(0));

            // HEX convert + '0' Padding
            const hex = ('00' + dec.toString(16)).slice(-2);

            // Append to cypher string
            cypher += hex;
        }

        return cypher;
    },
    decrypt: (cypherString, key) => {
        let plainText = '';
        const cypherArray = cypherString.match(/.{2}/g)

        // XOR Decrypt with provided cypher text and key
        for (let i = 0; i < cypherArray.length; i++) {
            const hex = cypherArray[i];
            const dec = parseInt(hex, 16);
            const keyPointer = i % key.length;
            const asciiCode = dec ^ (key[keyPointer]).charCodeAt(0);
            plainText += String.fromCharCode(asciiCode);
        }
        return plainText;
    }
}
