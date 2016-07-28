  <?php
    //Load header
    include_once ('inc_header.php');

    $link = connectToDB();

    $imagethumbpath = "images/uploads/gallery/thumbs/";
    $imagelargepath = "images/uploads/gallery/large/";

    setlocale(LC_ALL, 'sv_SE.ISO8859-1');
    $tz = new DateTimeZone('Europe/Stockholm');
    $year = 2016;
    $week = date("W");
    $weekdates = getStartAndEndDate($year, $week);
    $startdate = $weekdates['weekstart'];
    $enddate = $weekdates['weekend'];


  ?>
    <title>Media</title>
    <link rel="stylesheet" href="css/jquery.fancybox.css" type="text/css">
    <script type="text/javascript" src="js/isotope.pkgd.min.js"></script>
    <script type="text/javascript" src="js/jquery.fancybox.pack.js"></script>
    <script type="text/javascript" src="js/jquery.fancybox-media.js"></script>
    <script type="text/javascript" src="js/media.js"></script>
  </head>

  <body>

    <?php
      //Load top content
      include_once ('inc_top_content.php');
    ?>

    <div class="content-wrapper">
      <h1>Media</h1>

      <div class="filters">
        <div class="button-group filters-button-group" data-filter-group="type">
          <button class="button is-checked" data-filter="">Visa alla</button>
          <button class="button" data-filter=".filter-image">Bild</button>
          <button class="button" data-filter=".filter-video">Video</button>
        </div>

        <div class="button-group filters-button-group" data-filter-group="week">
          <button class="button is-checked" data-filter="">Visa alla</button>
          <button class="button" data-filter=".filter-33">33</button>
          <button class="button" data-filter=".filter-34">34</button>
          <button class="button" data-filter=".filter-35">35</button>
          <button class="button" data-filter=".filter-36">36</button>
        </div>

        <?php
        $query = "SELECT name FROM event";
        $result = execQuery($link, $query);
        ?>

        <div class="button-group filters-button-group" data-filter-group="event">
          <button class="button is-checked" data-filter="">Visa alla</button>
          <?php
          while ($event = $result->fetch_object()) {
            $name = $event->name;
            echo'<button class="button" data-filter=".filter-'.$name.'">'.$name.'</button>';
          }
          ?>
        </div>
      </div>
      <div class="grid">

        <?php
        // Images
        $query = "SELECT imagename, imagecreateddate, event, week FROM images ORDER BY imagecreateddate, imageorder ASC";
        $result = execQuery($link, $query);
        while ($image = $result->fetch_object()) {
          echo'
          <a class="fancybox-media" rel="gallery1" href="' . $imagelargepath . $image->imagename . '"><div class="filter-item filter-image filter-'.$image->week .' filter-'.$image->event .'" data-category="transition" style="background-image:url(' . $imagethumbpath . $image->imagename . ')">
          </div></a>';
        }

        // Video
        $query = "SELECT videoid, event FROM videos ORDER BY uploaddate ASC";
        $result = execQuery($link, $query);
        while ($video = $result->fetch_object()) {
          echo'
         <a class="fancybox-media" rel="gallery1" href="http://www.youtube.com/watch?v='.$video->videoid.'"><div class="filter-item filter-video filter-'.$video->event .'" data-category="transition" style="background-image:url(http://img.youtube.com/vi/' . $video->videoid . '/hqdefault.jpg)"><img class="video-play-icon" src="/design/play_icon.png" />
          </div></a>';
        }
    ?>
    </div>
    </div>

    <?php
      //Load footer
      include_once ('inc_footer.php');
    ?>

  </body>
</html>