const fs = require('fs');
const path = require('path');
const express = require('express');
const bodyParser = require('body-parser');
const JSZip = require('jszip');

const PORT = 7071;
let lastCode = '';

const app = express.createServer();
app.use(bodyParser.json({ limit: '50mb' }));

app.use(function(req, res, next) {
  res.header('Content-Type', 'application/json');
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
  next();
});

app.get('/callback', function(req, res) {
  if (req.query.code) {
    lastCode = req.query.code;
  }

  res.send(JSON.stringify({ success: true }));
});

app.get('/code', function(req, res) {
  res.send(JSON.stringify({ code: lastCode }));
});

app.post('/convert-bodymovin', async function(req, res) {
  const { data, filePath } = req.body;

  try {
    fs.writeFile(path.resolve(filePath), JSON.stringify(data), 'utf8', (error, success) => {
      res.send({
        status: 'success',
      });
    });
  } catch (error) {
    res.send({
      status: 'error',
      details: error.toString(),
    });
  }
});

// app.post('/convert-tgs', async function(req, res) {
//   const { data, filePath } = req.body;
//
//   try {
//     // const tgs = new TGSKit();
//     await tgs.load(data);
//
//     const errors = anim.validate();
//
//     if (errors.length === 0) {
//       fs.writeFile(path.resolve(filePath), tgs.generate(), 'binary', (error, success) => {
//         res.send({
//           status: 'success',
//         });
//       });
//     } else {
//       res.send({
//         status: 'error',
//         details: errors,
//       });
//     }
//   } catch (error) {
//     res.send({
//       status: 'error',
//       details: error.toString(),
//     });
//   }
// });

app.post('/convert-dotlottie', async function(req, res) {
  const { data, filePath } = req.body;

  try {
    const dotLottie = new JSZip();

    const manifest = {
      animations: [{ loop: true, themeColor: data.meta.tc, id: 'animation', speed: 1.0 }],
      author: data.meta.a,
      description: data.meta.d,
      generator: data.meta.g,
      keywords: data.meta.k,
      version: '1.0',
    };

    dotLottie.file('manifest.json', JSON.stringify(manifest));
    dotLottie.file('animations/animation.json', JSON.stringify(data));
    const dotLottieFile = await dotLottie.generateAsync({ type: 'nodebuffer', compression: 'DEFLATE' });

    fs.writeFile(path.resolve(filePath), dotLottieFile, 'binary', (error, success) => {
      res.send({
        status: 'success',
      });
    });
  } catch (error) {
    res.send({
      status: 'error',
      details: error.toString(),
    });
  }
});

app.listen(PORT);
