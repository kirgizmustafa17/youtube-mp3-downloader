_INVIDIOUS_SITES = (
    # invidious-redirect websites
    r'(?:www\.)?redirect\.invidious\.io',
    r'(?:(?:www|dev)\.)?invidio\.us',
    # Invidious instances taken from https://github.com/iv-org/documentation/blob/master/Invidious-Instances.md
    r'(?:(?:www|no)\.)?invidiou\.sh',
    r'(?:(?:www|fi)\.)?invidious\.snopyta\.org',
    r'(?:www\.)?invidious\.kabi\.tk',
    r'(?:www\.)?invidious\.13ad\.de',
    r'(?:www\.)?invidious\.mastodon\.host',
    r'(?:www\.)?invidious\.zapashcanon\.fr',
    r'(?:www\.)?(?:invidious(?:-us)?|piped)\.kavin\.rocks',
    r'(?:www\.)?invidious\.tinfoil-hat\.net',
    r'(?:www\.)?invidious\.himiko\.cloud',
    r'(?:www\.)?invidious\.reallyancient\.tech',
    r'(?:www\.)?invidious\.tube',
    r'(?:www\.)?invidiou\.site',
    r'(?:www\.)?invidious\.site',
    r'(?:www\.)?invidious\.xyz',
    r'(?:www\.)?invidious\.nixnet\.xyz',
    r'(?:www\.)?invidious\.048596\.xyz',
    r'(?:www\.)?invidious\.drycat\.fr',
    r'(?:www\.)?inv\.skyn3t\.in',
    r'(?:www\.)?tube\.poal\.co',
    r'(?:www\.)?tube\.connect\.cafe',
    r'(?:www\.)?vid\.wxzm\.sx',
    r'(?:www\.)?vid\.mint\.lgbt',
    r'(?:www\.)?vid\.puffyan\.us',
    r'(?:www\.)?yewtu\.be',
    r'(?:www\.)?yt\.elukerio\.org',
    r'(?:www\.)?yt\.lelux\.fi',
    r'(?:www\.)?invidious\.ggc-project\.de',
    r'(?:www\.)?yt\.maisputain\.ovh',
    r'(?:www\.)?ytprivate\.com',
    r'(?:www\.)?invidious\.13ad\.de',
    r'(?:www\.)?invidious\.toot\.koeln',
    r'(?:www\.)?invidious\.fdn\.fr',
    r'(?:www\.)?watch\.nettohikari\.com',
    r'(?:www\.)?invidious\.namazso\.eu',
    r'(?:www\.)?invidious\.silkky\.cloud',
    r'(?:www\.)?invidious\.exonip\.de',
    r'(?:www\.)?invidious\.riverside\.rocks',
    r'(?:www\.)?invidious\.blamefran\.net',
    r'(?:www\.)?invidious\.moomoo\.de',
    r'(?:www\.)?ytb\.trom\.tf',
    r'(?:www\.)?yt\.cyberhost\.uk',
    r'(?:www\.)?kgg2m7yk5aybusll\.onion',
    r'(?:www\.)?qklhadlycap4cnod\.onion',
    r'(?:www\.)?axqzx4s6s54s32yentfqojs3x5i7faxza6xo3ehd4bzzsg2ii4fv2iid\.onion',
    r'(?:www\.)?c7hqkpkpemu6e7emz5b4vyz7idjgdvgaaa3dyimmeojqbgpea3xqjoid\.onion',
    r'(?:www\.)?fz253lmuao3strwbfbmx46yu7acac2jz27iwtorgmbqlkurlclmancad\.onion',
    r'(?:www\.)?invidious\.l4qlywnpwqsluw65ts7md3khrivpirse744un3x7mlskqauz5pyuzgqd\.onion',
    r'(?:www\.)?owxfohz4kjyv25fvlqilyxast7inivgiktls3th44jhk3ej3i7ya\.b32\.i2p',
    r'(?:www\.)?4l2dgddgsrkf2ous66i6seeyi6etzfgrue332grh2n7madpwopotugyd\.onion',
    r'(?:www\.)?w6ijuptxiku4xpnnaetxvnkc5vqcdu7mgns2u77qefoixi63vbvnpnqd\.onion',
    r'(?:www\.)?kbjggqkzv65ivcqj6bumvp337z6264huv5kpkwuv6gu5yjiskvan7fad\.onion',
    r'(?:www\.)?grwp24hodrefzvjjuccrkw3mjq4tzhaaq32amf33dzpmuxe7ilepcmad\.onion',
    r'(?:www\.)?hpniueoejy4opn7bc4ftgazyqjoeqwlvh2uiku2xqku6zpoa4bf5ruid\.onion',
)
_VALID_URL = r"""(?x)^
                 (
                     (?:https?://|//)                                    # http(s):// or protocol-independent URL
                     (?:(?:(?:(?:\w+\.)?[yY][oO][uU][tT][uU][bB][eE](?:-nocookie|kids)?\.com|
                        (?:www\.)?deturl\.com/www\.youtube\.com|
                        (?:www\.)?pwnyoutube\.com|
                        (?:www\.)?hooktube\.com|
                        (?:www\.)?yourepeat\.com|
                        tube\.majestyc\.net|
                        %(invidious)s|
                        youtube\.googleapis\.com)/                        # the various hostnames, with wildcard subdomains
                     (?:.*?\#/)?                                          # handle anchor (#/) redirect urls
                     (?:                                                  # the various things that can precede the ID:
                         (?:(?:v|embed|e)/(?!videoseries))                # v/ or embed/ or e/
                         |shorts/
                         |(?:                                             # or the v= param in all its forms
                             (?:(?:watch|movie)(?:_popup)?(?:\.php)?/?)?  # preceding watch(_popup|.php) or nothing (like /?v=xxxx)
                             (?:\?|\#!?)                                  # the params delimiter ? or # or #!
                             (?:.*?[&;])??                                # any other preceding param (like /?s=tuff&v=xxxx or ?s=tuff&amp;v=V36LpHqtcDY)
                             v=
                         )
                     ))
                     |(?:
                        youtu\.be|                                        # just youtu.be/xxxx
                        vid\.plus|                                        # or vid.plus/xxxx
                        zwearz\.com/watch|                                # or zwearz.com/watch/xxxx
                        %(invidious)s
                     )/
                     |(?:www\.)?cleanvideosearch\.com/media/action/yt/watch\?videoId=
                     )
                 )?                                                       # all until now is optional -> you can pass the naked ID
                 (?P<id>[0-9A-Za-z_-]{11})                                # here is it! the YouTube video ID
                 (?(1).+)?                                                # if we found the ID, everything can follow
                 $""" % {
    'invidious': '|'.join(_INVIDIOUS_SITES),
}
