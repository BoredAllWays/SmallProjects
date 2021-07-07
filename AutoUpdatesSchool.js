const puppeteer = require('puppeteer');
const fs = require('fs')
const updates_2 = JSON.parse(fs.readFileSync('updates.json', 'utf8'));

async function stanton_website() {
  const browser = await puppeteer.launch({headless: true});
  const page = await browser.newPage();
  await page.goto('schoolsite.com');
  const hrefElement = await page.$('#module-content-61443 > div > div.ui-widget-header');
  await hrefElement.click();
  console.log('Clicked');
  updates1 = await page.$$eval('.headline-normal a',elements => elements.map(item => item.textContent));
  updates = await page.$$eval('.headline-normal a',elements => elements.map(item => item.getAttribute('href')));
  
  updated_sites_names = {};
  list1 = [];
  list2 = [];
  for(let i = 0; i < updates1.length; i++)
  {
    if (updates1[i] != 'Comments (-1)')
    {
      list1.push(updates1[i]);
    };
  }

  for(let i = 0; i < updates.length; i++) 
  {
    if (updates[i].substring(0,5) == "https") 
    {
      list2.push(updates[i]);
    }
  }

  for(let i = 0; i < list1.length; i++)
  {
    updated_sites_names[list1[i]] = list2[i];
  }

  console.log(updated_sites_names);
  
  browser.close();
}

setInterval(stanton_website, 3000);
