---
author: gbmhunter
date: 2012-10-07 01:09:09+00:00
draft: false
title: Rotating Image Banner Added
type: post
url: /site-admin/rotating-image-banner-added
categories:
- Site Admin
- Updates
tags:
- banner
- cimy
- cladlabs
- drupal
- header
- image
- rotating
---

Finally, a rotating image banner has been added back to CladLabs, just like the one when the website was running of the [Drupal CMS](http://drupal.org/). I used the [Cimy Header Image Rotator plugin](http://wordpress.org/extend/plugins/cimy-header-image-rotator/) and added code to the header.php file in a child theme for 'motion'.

{{< figure src="/images/misc/screenshot-of-banner-added-to-cladlabs.jpg" caption="Screenshot of the rotating banner added to the CladLabs website."  width="600px" >}}

I was having issues with the text element that the Cimy plugin added with the image. The default setting was for the text to be placed in the middle (both vertically and horizontally) of the image, which isn't very appealing. I wanted the text to span the bottom of the image, and wanted to get rid of the rounded corners of the text box. To do this, I had to edit the generated code as follows (including adding an extra 'div' element around the entire plugin). The total size of the rotating header element is 980x300px.

Note that CSS styling is included in this html file, as provided by the generated Cimy code. If I really wanted to do this 'properly', I would move the CSS to the style.css file in the same folder.

```html
<!-- Code added to header.php in the child theme for motion ('motion-child')
   Added in the header div element below the logo div -->

<!-- Rotating Cimy header banner image. Added by Geo. -->
<div id="extra-cimy-header">
   <div id="cimy_div_id_0">Loading images...
   </div>
   <div class="cimy_div_id_0_caption"></div>
   <style type="text/css">
   #cimy_div_id_0 {
      position: relative;
      float: left;
      margin: 1em auto;
      border: 1px solid #000000;
      width: 980px;
      height: 300px;
   }

   #extra-cimy-header {
      position: relative;
      float: left;
      margin: 0 auto;
      width: 980px;
      height: 300px;
      padding: 0px 0px 30px 0px;
   }

   div.cimy_div_id_0_caption {
      position: absolute; /* Added by Geo */
      /* margin-top: 0px; */
      margin-left: -490px;
      width: 980px;
      text-align: center;
      left: 50%;
      top: 281px;
      padding: 10px 0px;
      background: black;
      color: white;
      font-family: sans-serif;
      border-radius: 0px;
      display: none;
      z-index: 2;
   }
   </style>

   <noscript>
   <div id="cimy_div_id_0_nojs">
      <img id="cimy_img_id" src="http://blog.mbedded.ninja/wp-content/Cimy_Header_Images/0/12mhz-crystal-output-when-driven-by-microcontroller.jpg" alt="" />
   </div>
   </noscript>
</div>
<!-- End of rotating banner image -->
```