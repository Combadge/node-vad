{
    'targets': [
        {
            'target_name': 'vad',
            'defines': ["NAPI_VERSION=<(napi_build_version)",],
            'include_dirs': ["<!@(node -p \"require('node-addon-api').include\")", "<!(node -e \"require('nan')\")", "./src"],
            'sources': [
                'src/simplevad.c',
                'src/vad_bindings.cc'
            ],
            'dependencies': [
                "./vendor/webrtc_vad/webrtc_vad.gyp:webrtc_vad",
                "<!(node -p \"require('node-addon-api').gyp\")"
            ],
            'cflags!': [ '-fno-exceptions' ],
            'cflags_cc!': [ '-fno-exceptions' ],
            'xcode_settings': {
                'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
                'CLANG_CXX_LIBRARY': 'libc++',
                'MACOSX_DEPLOYMENT_TARGET': '11.0'
            },
            'msvs_settings': {
                'VCCLCompilerTool': { 'ExceptionHandling': 1 },
            }
        }
    ]
}
