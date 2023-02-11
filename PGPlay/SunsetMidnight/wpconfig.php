www-data@midnight:/$ cat /var/www/html/wordpress/wp-config.php 
<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress_db' );

/** MySQL database username */
define( 'DB_USER', 'jose' );

/** MySQL database password */
define( 'DB_PASSWORD', '645dc5a8871d2a4269d4cbe23f6ae103' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         '9F#)Pk/=&SyQ/>UVRBXx$}e&>G@(+m6L|_{Emur&fv&fO_+wbJ`-6QnE_7hI|Y<p');
define('SECURE_AUTH_KEY',  'p#Eh5#4W~p4-Iue2M)H/?[dp`BS;$7o~Kb%F?&S-Zv=rH#;U%`9G#VR`l^,8j$M+');
define('LOGGED_IN_KEY',    '0{YUw?X%j+ej-0du&FW@QkVP?b(#QsQfu[Q%<QS_Lpc1UI1|st:EJr)d*$g/iJ18');
define('NONCE_KEY',        '%)thH*l;)A^S#8WQ!8TKAnQ;uNXNKv<f.|PyYijgztda70y-4m~DTyqr^X!$JwX#');
define('AUTH_SALT',        '<Kd5.3^|yo:/fw2Y|PTb4!bU~5uRv7Z(n0;~jOXoO7MC]j/ICu[tY!)g4Oah-{oa');
define('SECURE_AUTH_SALT', 'dmYQvQ1Ap&z~JUHUaKR6]<rm7^ydGAp(/EH&+vrAi6cBpi?F7XKTc@Ahm:|h*wR;');
define('LOGGED_IN_SALT',   '5+Iw-;-j+2rD3WgRtSM`!zDb5I%LLU0]Awk-Cma:f4xrJv%k~/@+TthXY_[JpjfK');
define('NONCE_SALT',       'iDo3}y9z;@c~a)ZLT:7|.ZCp-0sK4>T1p&%MhGt_TUu+HFpPjn-no`:8sI0BA);y');

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
        define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';

